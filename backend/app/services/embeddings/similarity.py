import json
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(
    cv_embedding,
    job_embedding
):

    cv = np.array(
        json.loads(cv_embedding)
    ).reshape(1, -1)

    job = np.array(
        json.loads(job_embedding)
    ).reshape(1, -1)

    similarity = cosine_similarity(
        cv,
        job
    )[0][0]

    return float(similarity)