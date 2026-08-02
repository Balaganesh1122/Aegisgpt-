from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF
from docx import Document


class DocumentParser:
    """
    Service responsible for extracting text from supported documents.
    """

    @staticmethod
    def parse(file_path: str) -> Optional[str]:
        """
        Detect file type and extract text.
        """
        path = Path(file_path)

        extension = path.suffix.lower()

        if extension == ".pdf":
            return DocumentParser.parse_pdf(path)

        elif extension == ".docx":
            return DocumentParser.parse_docx(path)

        elif extension == ".txt":
            return path.read_text(encoding="utf-8")

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    @staticmethod
    def parse_pdf(file_path: Path) -> str:
        """
        Extract text from PDF using PyMuPDF.
        """
        text = ""

        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text

    @staticmethod
    def parse_docx(file_path: Path) -> str:
        """
        Extract text from DOCX.
        """
        document = Document(file_path)

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
        ]

        return "\n".join(paragraphs)