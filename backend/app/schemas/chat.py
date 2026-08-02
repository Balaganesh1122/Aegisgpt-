from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    conversation_id: int | None = None
    document_id: int
    top_k: int = 5


class ChatResponse(BaseModel):
    answer: str
    conversation_id: int