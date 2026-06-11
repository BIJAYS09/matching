from openai import OpenAI

from app.core.config import settings

from app.schemas.job_extraction import (
    JobExtraction
)

from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

def extract_job_information(raw_text: str):

    prompt = f"""
    Extract structured information from this job description.

    IMPORTANT:
    - Do NOT invent information
    - Return ONLY information present
    - Normalize terminology
    - Extract technologies carefully

    JOB DESCRIPTION:

    {raw_text[:12000]}
    """
    
    messages = [
    {
        "role": "system",
        "content": "You are an expert recruiter and job description parser."
    },
    {
        "role": "user",
        "content": prompt
    }
]

    completion = ChatGroq(model="llama-3.3-70b-versatile", 
                          temperature=0.3).with_structured_output(JobExtraction).invoke(messages)

    print("Raw extraction job:", completion)
    parsed = completion

    return parsed