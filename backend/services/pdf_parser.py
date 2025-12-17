from PyPDF2 import PdfReader
from fastapi import UploadFile, HTTPException


def extract_text_from_pdf(file: UploadFile) -> str:
    try:
        reader = PdfReader(file.file)
        text_parts = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)

        return "\n".join(text_parts)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
