from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

import numpy as np


model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


MANUAL_MAPPINGS = {

    "cpp": "C++",

    "c plus plus": "C++",

    "js": "JavaScript",

    "ts": "TypeScript",

    "ml": "Machine Learning",

    "ai": "Artificial Intelligence"
}


CANONICAL_SKILLS = [

    "Python",
    "C++",
    "JavaScript",
    "TypeScript",
    "Machine Learning",
    "Deep Learning",
    "React",
    "Docker",
    "Kubernetes",
    "AWS",
    "TensorFlow",
    "PyTorch",
    "Radar",
    "FPGA",
    "Signal Processing"
]


canonical_embeddings = model.encode(
    CANONICAL_SKILLS
)


def normalize_skill(skill: str):

    cleaned = skill.strip().lower()

    if cleaned in MANUAL_MAPPINGS:
        return MANUAL_MAPPINGS[cleaned]

    skill_embedding = model.encode([skill])

    similarities = cosine_similarity(
        skill_embedding,
        canonical_embeddings
    )[0]

    best_index = np.argmax(similarities)

    best_score = similarities[best_index]

    best_skill = CANONICAL_SKILLS[
        best_index
    ]

    if best_score > 0.75:
        return best_skill

    return skill


def normalize_skills(skills: list[str]):

    normalized = []

    seen = set()

    for skill in skills:

        normalized_skill = normalize_skill(
            skill
        )

        key = normalized_skill.lower()

        if key not in seen:

            normalized.append(
                normalized_skill
            )

            seen.add(key)

    return normalized