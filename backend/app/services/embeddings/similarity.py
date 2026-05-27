import json

import numpy as np

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def compute_similarity(
    embedding1,
    embedding2
):

    e1 = np.array(
        json.loads(embedding1)
    ).reshape(1, -1)

    e2 = np.array(
        json.loads(embedding2)
    ).reshape(1, -1)

    similarity = cosine_similarity(
        e1,
        e2
    )[0][0]

    return float(similarity)