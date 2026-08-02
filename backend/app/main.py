from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router
from app.api.v1.endpoints import documents
from app.api.v1.endpoints import search
from app.api.v1.endpoints import llm
from app.api.v1.endpoints import chat

app = FastAPI(
    title=settings.PROJECT_NAME
)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)

app.include_router(
    documents.router,
    prefix="/api/v1/documents",
    tags=["Documents"]
)

app.include_router(
    search.router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    llm.router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    chat.router,
    prefix=settings.API_V1_PREFIX,
)