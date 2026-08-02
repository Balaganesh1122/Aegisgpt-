from app.services.document_parser import DocumentParser
from app.services.text_chunker import TextChunker
from app.services.embedding_service import EmbeddingService


class IngestionService:

    def __init__(self):
        self.parser = DocumentParser()
        self.chunker = TextChunker()
        self.embedding = EmbeddingService()

    def process_document(self, file_path: str):

        text = self.parser.parse(file_path)

        chunks = self.chunker.chunk_text(text)

        embeddings = self.embedding.embed_documents(chunks)

        return chunks, embeddings