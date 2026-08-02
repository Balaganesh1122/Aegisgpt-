from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document_chunk import DocumentChunk


async def create_chunk(
    db: AsyncSession,
    document_id: int,
    chunk_index: int,
    content: str,
    embedding: list[float],
):
    chunk = DocumentChunk(
        document_id=document_id,
        chunk_index=chunk_index,
        content=content,
        embedding=embedding,
    )

    db.add(chunk)
    await db.commit()
    await db.refresh(chunk)

    return chunk


async def get_chunks(
    db: AsyncSession,
    document_id: int,
):
    result = await db.execute(
        select(DocumentChunk)
        .where(DocumentChunk.document_id == document_id)
        .order_by(DocumentChunk.chunk_index)
    )

    return result.scalars().all()