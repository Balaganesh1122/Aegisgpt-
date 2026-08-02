from pathlib import Path

import aiofiles
from fastapi import HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.document import create_document
from app.crud.document_chunk import create_chunk
from app.models.document import Document
from app.services.ingestion_service import IngestionService
from app.utils.file_utils import (
    generate_unique_filename,
    get_upload_path,
    is_allowed_file,
    validate_file_size,
)


class DocumentService:
    @staticmethod
    async def save_file(
        file: UploadFile,
        db: AsyncSession,
        uploaded_by: int,
    ):
        """
        Validate, save the file, store metadata,
        parse the document, generate embeddings,
        and store chunks in PostgreSQL.
        """

        # Validate file type
        if not is_allowed_file(file.filename):
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type."
            )

        # Read file
        content = await file.read()

        # Validate file size
        if not validate_file_size(len(content)):
            raise HTTPException(
                status_code=400,
                detail="File exceeds the 50 MB limit."
            )

        # Generate unique filename
        unique_filename = generate_unique_filename(file.filename)

        # Upload path
        upload_path: Path = get_upload_path(unique_filename)

        # Save file
        async with aiofiles.open(upload_path, "wb") as out_file:
            await out_file.write(content)

        # Save document metadata
        document = await create_document(
            db=db,
            filename=unique_filename,
            original_filename=file.filename,
            mime_type=file.content_type,
            size=len(content),
            storage_path=str(upload_path),
            uploaded_by=uploaded_by,
        )

        print("✅ File saved successfully")

        try:
            ingestion = IngestionService()

            print("✅ Ingestion service created")

            chunks, embeddings = ingestion.process_document(
                str(upload_path)
            )

            print(f"✅ Generated {len(chunks)} chunks")

            for index, (chunk, embedding) in enumerate(
                zip(chunks, embeddings)
            ):
                await create_chunk(
                    db=db,
                    document_id=document.id,
                    chunk_index=index,
                    content=chunk,
                    embedding=embedding,
                )

            print("✅ Chunks stored successfully")

            # ✅ IMPORTANT
            return document

        except Exception:
            import traceback

            traceback.print_exc()

            raise

    @staticmethod
    async def get_documents(db: AsyncSession):
        """
        Return all uploaded documents.
        """
        result = await db.execute(
            select(Document).order_by(
                Document.created_at.desc()
            )
        )

        return result.scalars().all()