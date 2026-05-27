import json

from app.services.scraper.parser import parse_job_page

from app.services.extraction.job_extractor import (
    extract_job_information
)

from app.services.embeddings.model import (
    create_embedding
)


def process_job(url: str):

    raw_text = parse_job_page(url)

    extracted = extract_job_information(raw_text)

    embedding = create_embedding(raw_text)

    return {

        "title": extracted.title,

        "company": extracted.company,

        "location": extracted.location,

        "url": url,

        "raw_text": raw_text,

        "summary": extracted.summary,

        "skills": json.dumps(extracted.skills),

        "technologies": json.dumps(
            extracted.technologies
        ),

        "education": json.dumps(
            extracted.education
        ),

        "responsibilities": json.dumps(
            extracted.responsibilities
        ),

        "experience_years": extracted.experience_years,

        "clearance": extracted.clearance,

        "citizenship": extracted.citizenship,

        "embedding": embedding
    }