from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.job import Job

from app.services.scraper.google_search import search_jobs
from app.services.scraper.parser import parse_job_page
from app.services.embeddings.model import create_embedding

router = APIRouter()


@router.post("/scrape-jobs")
def scrape_jobs(role: str):

    db: Session = SessionLocal()

    query = f"defense {role} jobs"

    urls = search_jobs(query)

    created = 0

    for url in urls:

        try:
            text = parse_job_page(url)

            embedding = create_embedding(text)

            job = Job(
                title=role,
                company="Unknown",
                location="Unknown",
                url=url,
                raw_text=text,
                embedding=embedding
            )

            db.add(job)
            created += 1

        except Exception as e:
            print(e)

    db.commit()

    return {
        "jobs_added": created
    }