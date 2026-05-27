from openai import OpenAI
from langchain_groq import ChatGroq
from app.core.config import settings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_explanation(cv_text, job_text, score):

    prompt = f"""
    You are an expert recruiter.

    Explain why this CV matches this job.

    IMPORTANT:
    - Use ONLY evidence from text.
    - Do NOT invent skills.
    - Mention missing skills.
    - Mention strengths.

    Match Score: {score}

    CV:
    {cv_text[:4000]}

    JOB:
    {job_text[:4000]}
    """

    response = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, max_tokens=1000).invoke(prompt)
    return response.text.strip()