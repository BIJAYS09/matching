from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.cv import CV
from app.db.models.job import Job

from app.services.embeddings.similarity import compute_similarity
from app.services.matching.explanation import generate_explanation

router = APIRouter()


@router.get("/match/{cv_id}")
def match_jobs(cv_id: int):

    db: Session = SessionLocal()

    cv = db.query(CV).filter(CV.id == cv_id).first()

    jobs = db.query(Job).all()

    results = []

    for job in jobs:

        score = compute_similarity(
            cv.embedding,
            job.embedding
        )

        explanation = generate_explanation(
            cv.raw_text,
            job.raw_text,
            score
        )

        results.append({
            "job_id": job.id,
            "url": job.url,
            "score": score,
            "explanation": explanation
        })
        
        print(f"Computed similarity for CV {cv_id} and Job {job.id}: {score}, explanation: {explanation}")

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:10]