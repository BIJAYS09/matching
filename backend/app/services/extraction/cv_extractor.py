from openai import OpenAI

from app.core.config import settings

from app.schemas.cv_extraction import (
    CVExtraction
)


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


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

    completion = client.beta.chat.completions.parse(

        model="gpt-4.1-mini",

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
        ],

        response_format=CVExtraction
    )

    parsed = completion.choices[0].message.parsed

    return parsed