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
        document_id: int,
        top_k: int = 8,
    ):
        rows = await self.retriever.retrieve(
            db=db,
            question=question,
            document_id=document_id,
            top_k=top_k,
        )

        contexts = [row.content for row in rows]

        # Debug: print retrieved chunks
        print("\n========== RETRIEVED CHUNKS ==========\n")
        for index, row in enumerate(rows):
            print(f"Chunk {index + 1}")
            print(row.content)
            print("--------------------------------------")

        prompt = PromptBuilder.build_prompt(
            question=question,
            contexts=contexts,
        )

        answer = self.llm.generate(prompt)

        sources = []

        for row in rows:
            sources.append(
                {
                    "document_id": row.document_id,
                    "chunk_index": row.chunk_index,
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }