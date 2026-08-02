from typing import List


class TextChunker:
    """
    Splits extracted text into overlapping chunks for RAG.
    """

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> List[str]:

        if not text.strip():
            return []

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(chunk.strip())

            start += chunk_size - chunk_overlap

        return chunks