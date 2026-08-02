from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.search import semantic_search
from app.services.embedding_service import EmbeddingService


class RetrievalService:

    def __init__(self):
        self.embedding = EmbeddingService()

    async def retrieve(
        self,
        db: AsyncSession,
        question: str,
        top_k: int = 5,
    ):
        # Generate embedding for the user's question
        query_embedding = self.embedding.embed_text(question)

        # Perform semantic search
        results = await semantic_search(
            db=db,
            embedding=query_embedding,
            limit=top_k,
        )

        return results