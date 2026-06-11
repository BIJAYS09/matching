from openai import OpenAI

from app.core.config import settings

from app.schemas.cv_extraction import (
    CVExtraction
)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


def extract_cv_information(raw_text: str):

    prompt = f"""
    Extract structured information from this CV.

    IMPORTANT:
    - Do NOT invent information
    - Return ONLY information present
    - Normalize technologies
    - Extract skills carefully
    - Extract experience accurately

    CV:

    {raw_text[:12000]}
    """
    
    messages=[

            {
                "role": "system",
                "content": (
                    "You are an expert technical recruiter "
                    "and CV parser."
                )
            },

            {
                "role": "user",
                "content": prompt
            }
        ]
    
    completion = ChatGroq(model="llama-3.3-70b-versatile", 
                          temperature=0.3).with_structured_output(CVExtraction).invoke(messages)
 

    print("Raw CV Extraction Response:", completion)
    parsed = completion

    return parsed