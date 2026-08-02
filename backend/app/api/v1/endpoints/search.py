from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.schemas.search import SearchRequest, SearchResponse, SearchResult
from app.services.retrieval_service import RetrievalService

router = APIRouter(prefix="/search", tags=["Semantic Search"])


@router.post(
    "",
    response_model=SearchResponse,
)
async def semantic_search_endpoint(
    request: SearchRequest,
    db: AsyncSession = Depends(get_db),
):
    retrieval = RetrievalService()

    rows = await retrieval.retrieve(
        db=db,
        question=request.query,
        top_k=request.top_k,
    )

    results = []

    for row in rows:
        results.append(
            SearchResult(
                document_id=row.document_id,
                chunk_index=row.chunk_index,
                content=row.content,
                score=float(row.distance),
            )
        )

    return SearchResponse(results=results)