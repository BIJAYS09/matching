import json

from app.services.embeddings.similarity import (
    compute_similarity
)

from app.services.extraction.semantic_matcher import (
    semantic_match_analysis
)


def calculate_skill_overlap(

    candidate_skills,

    required_skills
):

    if not required_skills:
        return 0.0

    candidate_set = set(
        skill.lower()
        for skill in candidate_skills
    )

    required_set = set(
        skill.lower()
        for skill in required_skills
    )

    overlap = candidate_set.intersection(
        required_set
    )

    return len(overlap) / len(required_set)


def calculate_experience_score(

    candidate_experience,

    required_experience
):

    if not required_experience:
        return 0.5

    try:

        candidate_years = float(
            candidate_experience
        )

        required_years = float(
            required_experience
        )

        if candidate_years >= required_years:
            return 1.0

        return candidate_years / required_years

    except:
        return 0.5


def calculate_education_score(

    candidate_education,

    required_education
):

    if not required_education:
        return 0.5

    candidate_text = " ".join(
        candidate_education
    ).lower()

    required_text = " ".join(
        required_education
    ).lower()

    if required_text in candidate_text:
        return 1.0

    return 0.5


def hybrid_match(

    cv,

    job
):

    candidate_skills = json.loads(
        cv.skills or "[]"
    )

    required_skills = json.loads(
        job.skills or "[]"
    )

    candidate_education = json.loads(
        cv.education or "[]"
    )

    required_education = json.loads(
        job.education or "[]"
    )

    # ---------------------------------
    # Semantic similarity
    # ---------------------------------

    semantic_similarity = compute_similarity(

        cv.embedding,

        job.embedding
    )

    # ---------------------------------
    # Skill overlap
    # ---------------------------------

    skill_overlap = calculate_skill_overlap(

        candidate_skills,

        required_skills
    )

    # ---------------------------------
    # Experience match
    # ---------------------------------

    experience_match = calculate_experience_score(

        cv.years_experience,

        job.experience_years
    )

    # ---------------------------------
    # Education match
    # ---------------------------------

    education_match = calculate_education_score(

        candidate_education,

        required_education
    )

    # ---------------------------------
    # Final weighted score
    # ---------------------------------

    final_score = (

        semantic_similarity * 0.35 +

        skill_overlap * 0.30 +

        experience_match * 0.20 +

        education_match * 0.05 +

        0.10
    )

    # ---------------------------------
    # LLM reasoning layer
    # ---------------------------------

    reasoning = semantic_match_analysis(

        candidate_skills,

        required_skills
    )

    return {

        "semantic_similarity": round(
            semantic_similarity,
            3
        ),

        "skill_overlap": round(
            skill_overlap,
            3
        ),

        "experience_match": round(
            experience_match,
            3
        ),

        "education_match": round(
            education_match,
            3
        ),

        "final_score": round(
            final_score,
            3
        ),

        "reasoning": reasoning
    }