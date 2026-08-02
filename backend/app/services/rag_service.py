from sqlalchemy.ext.asyncio import AsyncSession

from app.services.retrieval_service import RetrievalService
from app.services.prompt_builder import PromptBuilder
from app.services.llm_service import LLMService


class RAGService:

    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()

    async def ask(
        self,
        db: AsyncSession,
        question: str,
        top_k: int = 5,
    ):

        rows = await self.retriever.retrieve(
            db=db,
            question=question,
            top_k=top_k,
        )

        contexts = [row.content for row in rows]

        prompt = PromptBuilder.build_prompt(
            question=question,
            contexts=contexts,
        )

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "contexts": contexts,
        }