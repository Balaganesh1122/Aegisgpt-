from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document


async def create_document(
    db: AsyncSession,
    filename: str,
    original_filename: str,
    mime_type: str,
    size: int,
    storage_path: str,
    uploaded_by: int,
) -> Document:

    document = Document(
        filename=filename,
        original_filename=original_filename,
        mime_type=mime_type,
        size=size,
        storage_path=storage_path,
        uploaded_by=uploaded_by,
    )

    db.add(document)
    await db.commit()
    await db.refresh(document)

    return document


async def get_document(
    db: AsyncSession,
    document_id: int,
) -> Document | None:

    result = await db.execute(
        select(Document).where(
            Document.id == document_id
        )
    )

    return result.scalar_one_or_none()


async def get_documents(db: AsyncSession):

    result = await db.execute(
        select(Document).order_by(
            Document.created_at.desc()
        )
    )

    return result.scalars().all()


async def delete_document(
    db: AsyncSession,
    document: Document,
):

    await db.delete(document)
    await db.commit()