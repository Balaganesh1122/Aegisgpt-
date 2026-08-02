class PromptBuilder:
    """
    Builds prompts for Retrieval-Augmented Generation (RAG).
    """

    @staticmethod
    def build_prompt(
        question: str,
        contexts: list[str],
    ) -> str:

        context = "\n\n".join(contexts)

        return f"""
You are AegisGPT, an AI assistant for document question answering.

Instructions:

- Answer ONLY using the provided context.
- If the answer is not present in the context, reply exactly:
  "I couldn't find that information in the uploaded documents."
- Do not make up facts.
- Keep answers clear and professional.

==========================
CONTEXT
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================
"""