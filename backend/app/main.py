from fastapi import FastAPI

from app.api.routes import cv
from app.api.routes import jobs
from app.api.routes import matching

app = FastAPI(
    title="Defense CV Matching API"
)



from app.db.base import Base
from app.db.session import engine


Base.metadata.create_all(bind=engine)


app.include_router(cv.router)
app.include_router(jobs.router)
app.include_router(matching.router)