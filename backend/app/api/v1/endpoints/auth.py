from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    Token,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        user = await AuthService.register(
            db=db,
            full_name=request.full_name,
            email=request.email,
            password=request.password,
        )

        return user

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=Token,
)
async def login(
    request: UserLogin,
    db: AsyncSession = Depends(get_db),
):
    result = await AuthService.login(
        db=db,
        email=request.email,
        password=request.password,
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password.",
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
    }