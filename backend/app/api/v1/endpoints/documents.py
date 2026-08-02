from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.document import DocumentUploadResponse
from app.services.document_service import DocumentService

router = APIRouter()


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=201,
)
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    document = await DocumentService.save_file(
        file=file,
        db=db,
        uploaded_by=1,   # Temporary until authentication is added
    )

    return {
        "message": "Document uploaded successfully",
        "document": document,
    }