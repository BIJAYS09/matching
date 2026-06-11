import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.db.models.cv import CV

from app.services.cv.process_cv import (
    process_cv
)

router = APIRouter()


@router.post("/upload-cv")

async def upload_cv(

    file: UploadFile = File(...)
):

    os.makedirs(
        "tmp",
        exist_ok=True
    )

    file_path = f"tmp/{file.filename}"

    with open(file_path, "wb") as f:

        f.write(await file.read())

    data = process_cv(file_path)

    db: Session = SessionLocal()

    cv = CV(**data)

    db.add(cv)

    db.commit()

    db.refresh(cv)
    
    print("CV Processed and Saved:", cv.id)

    return {

        "cv_id": cv.id,

        "candidate_name": cv.candidate_name,

        "skills": data["skills"]
    }