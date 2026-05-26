import json

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def create_embedding(text: str):

    embedding = model.encode(text).tolist()

    return json.dumps(embedding)