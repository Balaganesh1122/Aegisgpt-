from pydantic import BaseModel


class Source(BaseModel):
    document_id: int
    chunk_index: int


class ChatRequest(BaseModel):
    question: str
    conversation_id: int | None = None
    document_id: int
    top_k: int = 10


class ChatResponse(BaseModel):
    answer: str
    conversation_id: int
    sources: list[Source] = []