from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from app.db.base import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    company = Column(String)

    location = Column(String)

    url = Column(String)

    raw_text = Column(Text)

    summary = Column(Text)

    skills = Column(Text)

    technologies = Column(Text)

    education = Column(Text)

    responsibilities = Column(Text)

    experience_years = Column(String)

    clearance = Column(String)

    citizenship = Column(String)

    embedding = Column(Text)