from fastapi import APIRouter, UploadFile, File
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.cv import CV
from app.utils.pdf import extract_pdf_text
from app.services.embeddings.model import create_embedding

router = APIRouter()


@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    path = f"tmp/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = extract_pdf_text(path)

    embedding = create_embedding(text)

    db: Session = SessionLocal()

    cv = CV(
        candidate_name=file.filename,
        raw_text=text,
        embedding=embedding
    )

    db.add(cv)
    db.commit()
    db.refresh(cv)

    return {
        "cv_id": cv.id,
        "message": "CV uploaded successfully"
    }