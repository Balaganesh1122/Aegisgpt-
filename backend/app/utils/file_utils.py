import os
import uuid
from pathlib import Path

# Base upload directory
UPLOAD_DIR = Path("storage/uploads")

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".txt",
    ".csv",
    ".xlsx",
    ".md",
}

# Maximum file size (50 MB)
MAX_FILE_SIZE = 50 * 1024 * 1024


def ensure_upload_directory() -> None:
    """
    Create the upload directory if it doesn't exist.
    """
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def get_file_extension(filename: str) -> str:
    """
    Returns the file extension in lowercase.
    """
    return Path(filename).suffix.lower()


def is_allowed_file(filename: str) -> bool:
    """
    Check if the uploaded file has an allowed extension.
    """
    return get_file_extension(filename) in ALLOWED_EXTENSIONS


def generate_unique_filename(original_filename: str) -> str:
    """
    Generate a UUID filename while preserving the extension.
    """
    extension = get_file_extension(original_filename)
    return f"{uuid.uuid4()}{extension}"


def get_upload_path(filename: str) -> Path:
    """
    Returns the full upload path.
    """
    ensure_upload_directory()
    return UPLOAD_DIR / filename


def validate_file_size(file_size: int) -> bool:
    """
    Returns True if the file size is within the allowed limit.
    """
    return file_size <= MAX_FILE_SIZE