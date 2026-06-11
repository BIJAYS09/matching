from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.db.models.cv import CV

from app.db.models.job import Job

from app.services.matching.hybrid_matcher import (
    hybrid_match
)

router = APIRouter()


# -----------------------------------
# Get all CVs
# -----------------------------------

@router.get("/cvs")

def get_cvs():

    db: Session = SessionLocal()

    cvs = db.query(CV).all()

    return [

        {
            "id": cv.id,
            "name": cv.candidate_name,
            "email": cv.email,
            "skills": cv.skills
        }

        for cv in cvs
    ]


# -----------------------------------
# Get all jobs
# -----------------------------------

@router.get("/jobs")

def get_jobs():

    db: Session = SessionLocal()

    jobs = db.query(Job).all()

    return [

        {
            "id": job.id,
            "title": job.title,
            "company": job.company,
            "location": job.location
        }

        for job in jobs
    ]


# -----------------------------------
# Match CV against all jobs
# -----------------------------------

@router.get("/matches/{cv_id}")

def get_matches(cv_id: int):

    db: Session = SessionLocal()

    cv = db.query(CV).filter(
        CV.id == cv_id
    ).first()

    jobs = db.query(Job).all()

    results = []

    for job in jobs:

        match_result = hybrid_match(
            cv,
            job
        )

        results.append({

            "job_id": job.id,

            "title": job.title,

            "company": job.company,

            "location": job.location,

            "url": job.url,

            **match_result
        })

    results.sort(

        key=lambda x: x["final_score"],

        reverse=True
    )

    return results[:10]