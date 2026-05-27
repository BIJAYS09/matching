from openai import OpenAI

from app.core.config import settings

from app.schemas.job_extraction import (
    JobExtraction
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


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

    completion = client.beta.chat.completions.parse(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": (
                    "You are an expert recruiter and "
                    "job description parser."
                )
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        response_format=JobExtraction
    )

    parsed = completion.choices[0].message.parsed

    return parsed