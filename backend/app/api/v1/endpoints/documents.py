from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import DocumentService
from app.api.dependencies.auth import get_current_user
from app.models.user import User
router = APIRouter()


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=201,
)
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    document = await DocumentService.save_file(
        file=file,
        db=db,
        uploaded_by=current_user.id,   # Temporary until authentication is added
    )

    return {
        "message": "Document uploaded successfully",
        "document": document,
    }


@router.get("/")
async def list_documents(
    db: AsyncSession = Depends(get_db),
):
    documents = await DocumentService.get_documents(db)

    return documents