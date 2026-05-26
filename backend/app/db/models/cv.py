from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True, index=True)

    candidate_name = Column(String)

    raw_text = Column(Text)

    embedding = Column(Text)