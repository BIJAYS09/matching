from pydantic import BaseModel
from typing import List, Optional


class JobExtraction(BaseModel):

    title: Optional[str] = None

    company: Optional[str] = None

    location: Optional[str] = None

    summary: Optional[str] = None

    skills: List[str] = []

    technologies: List[str] = []

    education: List[str] = []

    responsibilities: List[str] = []

    experience_years: Optional[str] = None

    clearance: Optional[str] = None

    citizenship: Optional[str] = None