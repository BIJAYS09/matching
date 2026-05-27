from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
)

from app.db.base import Base


class CV(Base):

    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True)

    candidate_name = Column(String)

    email = Column(String)

    phone = Column(String)

    location = Column(String)

    raw_text = Column(Text)

    summary = Column(Text)

    skills = Column(Text)

    technologies = Column(Text)

    education = Column(Text)

    certifications = Column(Text)

    languages = Column(Text)

    years_experience = Column(String)

    experience = Column(Text)

    projects = Column(Text)

    embedding = Column(Text)