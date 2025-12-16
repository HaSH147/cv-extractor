import pdfplumber

from fastapi import UploadFile, HTTPException

  
  

def extract_text_from_pdf(file: UploadFile) -> str:

    try:

        text_parts = []

        with pdfplumber.open(file.file) as pdf:

            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:

                    text_parts.append(page_text)

        return "\n".join(text_parts)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))