from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def semantic_search(
    db: AsyncSession,
    embedding: list[float],
    document_id: int,
    limit: int = 5,
):
    query = text("""
        SELECT
            id,
            document_id,
            chunk_index,
            content,
            embedding <=> CAST(:embedding AS vector) AS distance
        FROM document_chunks
        WHERE document_id = :document_id
        ORDER BY embedding <=> CAST(:embedding AS vector)
        LIMIT :limit;
    """)

    result = await db.execute(
        query,
        {
            "embedding": str(embedding),
            "document_id": document_id,
            "limit": limit,
        },
    )

    return result.fetchall()