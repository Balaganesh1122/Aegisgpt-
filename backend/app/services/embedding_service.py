from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings using a single shared SentenceTransformer model.
    The model is loaded only once when the application starts.
    """

    # Shared model instance (Singleton)
    _model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    def __init__(self):
        self.model = EmbeddingService._model

    def embed_text(self, text: str) -> list[float]:
        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_documents(
        self,
        documents: list[str],
    ) -> list[list[float]]:
        embeddings = self.model.encode(
            documents,
            normalize_embeddings=True,
        )

        return embeddings.tolist()