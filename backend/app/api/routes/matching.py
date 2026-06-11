from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.db.models.cv import CV

from app.db.models.job import Job

from app.services.matching.hybrid_matcher import (
    hybrid_match
)

router = APIRouter()


@router.get("/match/{cv_id}")

def match_jobs(cv_id: int):

    db: Session = SessionLocal()

    cv = db.query(CV).filter(
        CV.id == cv_id
    ).first()

    jobs = db.query(Job).all()

    results = []

    for job in jobs:

        result = hybrid_match(
            cv,
            job
        )

        results.append({

            "job_id": job.id,

            "title": job.title,

            "company": job.company,

            "location": job.location,

            "url": job.url,
            
            "skills": job.skills,

            **result
        })

    results.sort(

        key=lambda x: x["final_score"],

        reverse=True
    )

    return results[:10]