from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.db.models.job import Job

from app.services.jobs.process_job import (
    process_job
)

router = APIRouter()


@router.post("/add-job")

def add_job(url: str):

    db: Session = SessionLocal()

    data = process_job(url)

    job = Job(**data)

    db.add(job)

    db.commit()

    db.refresh(job)

    return {
        "job_id": job.id,
        "title": job.title,
        "company": job.company
    }