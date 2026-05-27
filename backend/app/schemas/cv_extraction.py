from pydantic import BaseModel

from typing import List, Optional


class ExperienceItem(BaseModel):

    company: Optional[str] = None

    role: Optional[str] = None

    duration: Optional[str] = None

    description: Optional[str] = None


class ProjectItem(BaseModel):

    name: Optional[str] = None

    description: Optional[str] = None

    technologies: List[str] = []


class CVExtraction(BaseModel):

    name: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    location: Optional[str] = None

    summary: Optional[str] = None

    skills: List[str] = []

    technologies: List[str] = []

    education: List[str] = []

    certifications: List[str] = []

    languages: List[str] = []

    years_experience: Optional[str] = None

    experience: List[ExperienceItem] = []

    projects: List[ProjectItem] = []