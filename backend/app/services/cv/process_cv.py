import json

from app.utils.pdf import (
    extract_pdf_text
)

from app.services.extraction.cv_extractor import (
    extract_cv_information
)

from app.services.extraction.skill_normalizer import (
    normalize_skills
)

from app.services.embeddings.model import (
    create_embedding
)


def process_cv(file_path: str):

    raw_text = extract_pdf_text(file_path)

    extracted = extract_cv_information(
        raw_text
    )

    normalized_skills = normalize_skills(
        extracted.skills
    )

    embedding = create_embedding(raw_text)

    return {

        "candidate_name": extracted.name,

        "email": extracted.email,

        "phone": extracted.phone,

        "location": extracted.location,

        "raw_text": raw_text,

        "summary": extracted.summary,

        "skills": json.dumps(
            normalized_skills
        ),

        "technologies": json.dumps(
            extracted.technologies
        ),

        "education": json.dumps(
            extracted.education
        ),

        "certifications": json.dumps(
            extracted.certifications
        ),

        "languages": json.dumps(
            extracted.languages
        ),

        "years_experience": extracted.years_experience,

        "experience": json.dumps([
            item.model_dump()
            for item in extracted.experience
        ]),

        "projects": json.dumps([
            item.model_dump()
            for item in extracted.projects
        ]),

        "embedding": embedding
    }