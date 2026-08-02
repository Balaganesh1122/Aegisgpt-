from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.conversation import (
    create_conversation,
    get_conversation,
    get_user_conversations,
)
from app.crud.message import (
    create_message,
    get_messages,
)


class ConversationService:

    async def start_conversation(
        self,
        db: AsyncSession,
        title: str,
        user_id: int,
        document_id: int,
    ):
        return await create_conversation(
            db=db,
            title=title,
            user_id=user_id,
            document_id=document_id,
        )

    async def save_user_message(
        self,
        db: AsyncSession,
        conversation_id: int,
        content: str,
    ):
        return await create_message(
            db=db,
            conversation_id=conversation_id,
            role="user",
            content=content,
        )

    async def save_ai_message(
        self,
        db: AsyncSession,
        conversation_id: int,
        content: str,
    ):
        return await create_message(
            db=db,
            conversation_id=conversation_id,
            role="assistant",
            content=content,
        )

    async def load_messages(
        self,
        db: AsyncSession,
        conversation_id: int,
    ):
        return await get_messages(
            db=db,
            conversation_id=conversation_id,
        )

    async def get_conversation(
        self,
        db: AsyncSession,
        conversation_id: int,
    ):
        return await get_conversation(
            db=db,
            conversation_id=conversation_id,
        )

    async def get_user_conversations(
        self,
        db: AsyncSession,
        user_id: int,
    ):
        return await get_user_conversations(
            db=db,
            user_id=user_id,
        )