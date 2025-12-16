from fastapi import FastAPI, UploadFile, HTTPException

from services.pdf_parser import extract_text_from_pdf
from services.docx_parser import extract_text_from_docx
from services.extractor import TextExtractor
from models.cv_result import CVResult


app = FastAPI()


@app.post("/api/v1/upload-cv", response_model=CVResult)
def upload_cv(file: UploadFile):
    if not file or not file.filename:
        raise HTTPException(status_code=400, detail="Pas de fichier fourni")

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)

    else:
        raise HTTPException(status_code=400, detail="Ce type de fichier n'est pas pris en charge")

    extractor = TextExtractor()
    result = extractor.extract_all(text)

    return CVResult(
    first_name=result["first_name"],
    last_name=result["last_name"],
    email=result["email"],
    phone=result["phone"],
    degree=result["degree"]
)
