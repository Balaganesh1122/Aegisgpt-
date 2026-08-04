from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Lazy-loaded singleton embedding model.
    The model loads only when first used.
    """

    _model = None

    @classmethod
    def get_model(cls):
        if cls._model is None:
            print("Loading embedding model...")
            cls._model = SentenceTransformer(
                "BAAI/bge-small-en-v1.5"
            )
            print("Embedding model loaded.")

        return cls._model

    def embed_text(self, text: str) -> list[float]:
        model = self.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    def embed_documents(
        self,
        documents: list[str],
    ) -> list[list[float]]:

        model = self.get_model()

        embeddings = model.encode(
            documents,
            normalize_embeddings=True,
        )

        return embeddings.tolist()