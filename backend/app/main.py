from fastapi import FastAPI

from app.db.base import Base

from app.db.session import engine

from app.db.models.job import Job

from app.db.models.cv import CV

from app.api.routes import jobs

from app.api.routes import cv


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs.router)

app.include_router(cv.router)