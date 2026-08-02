from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation


async def create_conversation(
    db: AsyncSession,
    title: str,
    user_id: int,
    document_id: int,
) -> Conversation:

    conversation = Conversation(
        title=title,
        user_id=user_id,
        document_id=document_id,
    )

    db.add(conversation)

    await db.commit()

    await db.refresh(conversation)

    return conversation


async def get_conversation(
    db: AsyncSession,
    conversation_id: int,
):

    result = await db.execute(
        select(Conversation).where(
            Conversation.id == conversation_id
        )
    )

    return result.scalar_one_or_none()


async def get_user_conversations(
    db: AsyncSession,
    user_id: int,
):

    result = await db.execute(
        select(Conversation).where(
            Conversation.user_id == user_id
        )
    )

    return result.scalars().all()