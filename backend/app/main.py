from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.router import api_router
from app.api.v1.endpoints import documents
from app.api.v1.endpoints import search
from app.api.v1.endpoints import llm
from app.api.v1.endpoints import chat
from app.api.v1.endpoints import auth
app = FastAPI(
    title=settings.PROJECT_NAME
)

# -------------------------
# CORS
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Routers
# -------------------------

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

app.include_router(
    auth.router,
    prefix=settings.API_V1_PREFIX,
)