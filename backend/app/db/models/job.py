from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    company = Column(String)

    location = Column(String)

    url = Column(String)

    raw_text = Column(Text)

    embedding = Column(Text)