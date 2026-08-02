from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation_service import ConversationService
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/chat",
    tags=["RAG Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    db: AsyncSession = Depends(get_db),
):
    rag = RAGService()
    conversation_service = ConversationService()

    conversation_id = request.conversation_id

    # Create a new conversation if this is the first message
    if conversation_id is None:
        conversation = await conversation_service.start_conversation(
            db=db,
            title=request.question[:50],
            user_id=1,          # Temporary until JWT authentication
            document_id=request.document_id,
        )
        conversation_id = conversation.id

    # Save user message
    await conversation_service.save_user_message(
        db=db,
        conversation_id=conversation_id,
        content=request.question,
    )

    # Generate RAG answer
    result = await rag.ask(
        db=db,
        question=request.question,
        top_k=request.top_k,
    )

    # Save AI response
    await conversation_service.save_ai_message(
        db=db,
        conversation_id=conversation_id,
        content=result["answer"],
    )

    return ChatResponse(
        answer=result["answer"],
        conversation_id=conversation_id,
    )