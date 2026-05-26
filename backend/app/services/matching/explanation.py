from openai import OpenAI
from app.core.config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_explanation(cv_text, job_text, score):

    prompt = f"""
    You are an expert defense recruiter.

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

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content