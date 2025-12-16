from fastapi import UploadFile, HTTPException
from docx import Document


def extract_text_from_docx(file: UploadFile) -> str:
    try:
        document = Document(file.file)

        text_parts = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                text_parts.append(paragraph.text)


        return "\n".join(text_parts)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
