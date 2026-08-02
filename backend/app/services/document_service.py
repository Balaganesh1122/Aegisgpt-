from pathlib import Path

import aiofiles
from fastapi import HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.document import create_document
from app.crud.document_chunk import create_chunk
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

        # -----------------------------
        # AI Ingestion Pipeline
        # -----------------------------

        ingestion = IngestionService()

        chunks, embeddings = ingestion.process_document(
            str(upload_path)
        )

        # Store chunks in PGVector
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

        return document