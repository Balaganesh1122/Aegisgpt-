import logging

from google import genai
from google.genai import types

from app.core.config import settings

logger = logging.getLogger(__name__)


class LLMService:
    """
    Google Gemini LLM Service
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )
        self.model = settings.GEMINI_MODEL

    def generate(self, prompt: str) -> str:
        """
        Generate a response from Gemini.
        """

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    max_output_tokens=1024,
                ),
            )

            if response.text:
                return response.text

            return "No response generated."

        except Exception as e:
            logger.exception("Gemini API Error")

            return (
                f"LLM Error: {type(e).__name__}: {str(e)}"
            )