from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.crud.user import (
    create_user,
    get_user_by_email,
)


class AuthService:
    @staticmethod
    async def register(
        db: AsyncSession,
        full_name: str,
        email: str,
        password: str,
    ):
        existing_user = await get_user_by_email(
            db,
            email,
        )

        if existing_user:
            raise ValueError("Email already exists.")

        user = await create_user(
            db=db,
            full_name=full_name,
            email=email,
            hashed_password=hash_password(password),
        )

        return user

    @staticmethod
    async def login(
        db: AsyncSession,
        email: str,
        password: str,
    ):
        user = await get_user_by_email(
            db,
            email,
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.hashed_password,
        ):
            return None

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user,
        }