from fastapi import APIRouter

from app.services.llm_service import LLMService

router = APIRouter(
    prefix="/llm",
    tags=["Gemini Test"],
)


@router.get("/test")
async def test_llm():

    llm = LLMService()

    response = llm.generate(
        "Say hello in one sentence."
    )

    return {
        "response": response
    }