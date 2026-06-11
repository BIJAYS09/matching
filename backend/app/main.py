from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.db.base import Base
from app.db.session import engine

from app.api.routes import jobs
from app.api.routes import cv
from app.api.routes import matching


Base.metadata.create_all(bind=engine)

app = FastAPI()


# ------------------------------------
# CORS
# ------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:3002"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

from app.api.routes import dashboard

app.include_router(dashboard.router)

app.include_router(jobs.router)

app.include_router(cv.router)

app.include_router(matching.router)