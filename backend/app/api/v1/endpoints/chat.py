from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.auth import get_current_user
from app.database.session import get_db
from app.models.user import User
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
    current_user: User = Depends(get_current_user),
):
    rag = RAGService()
    conversation_service = ConversationService()

    conversation_id = request.conversation_id

    # Create a new conversation if this is the first message
    if conversation_id is None:
        conversation = await conversation_service.start_conversation(
            db=db,
            title=request.question[:50],
            user_id=current_user.id,
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
        document_id=request.document_id,
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


@router.get("/conversations")
async def get_conversations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation_service = ConversationService()

    conversations = await conversation_service.get_user_conversations(
        db=db,
        user_id=current_user.id,
    )

    return conversations


@router.get("/conversations/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation_service = ConversationService()

    # Verify conversation belongs to logged-in user
    conversation = await conversation_service.get_conversation(
        db=db,
        conversation_id=conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        )

    if conversation.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied.",
        )

    messages = await conversation_service.load_messages(
        db=db,
        conversation_id=conversation_id,
    )

    return messages