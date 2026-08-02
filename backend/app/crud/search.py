from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def semantic_search(
    db: AsyncSession,
    embedding: list[float],
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
        ORDER BY embedding <=> CAST(:embedding AS vector)
        LIMIT :limit;
    """)

    result = await db.execute(
        query,
        {
            "embedding": str(embedding),
            "limit": limit,
        },
    )

    return result.fetchall()