import pdfplumber
import docx
from typing import IO, Union

def extract_text_from_pdf(file: IO[bytes]) -> str:
    """
    Extracts text from a PDF file stream.

    Args:
        file: A file-like object opened in binary mode.

    Returns:
        A string containing the extracted text.
    """
    try:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text.strip()
    except Exception as e:
        # You can add more specific error handling or logging here
        print(f"Error extracting text from PDF: {e}")
        return ""

def extract_text_from_docx(file: IO[bytes]) -> str:
    """
    Extracts text from a DOCX file stream.

    Args:
        file: A file-like object opened in binary mode.

    Returns:
        A string containing the extracted text.
    """
    try:
        document = docx.Document(file)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from DOCX: {e}")
        return ""

def extract_text(file: IO[bytes], filename: str) -> str:
    """
    Extracts text from a file based on its extension.

    Args:
        file: A file-like object (e.g., from an upload) opened in binary mode.
        filename: The original name of the file, used to determine the file type.

    Returns:
        The extracted text as a string, or an empty string if extraction fails
        or the file type is unsupported.
    """
    if filename.lower().endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.lower().endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        # For simplicity, we can return an error message or just empty string
        print(f"Unsupported file type: {filename}")
        return ""