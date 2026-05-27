from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def semantic_match_analysis(

    candidate_skills,

    required_skills
):

    prompt = f"""
    Compare candidate skills with job skills.

    IMPORTANT:
    - Consider transferable skills
    - Consider adjacent technologies
    - Do NOT invent experience

    Candidate Skills:
    {candidate_skills}

    Required Skills:
    {required_skills}

    Return:
    - matching skills
    - transferable skills
    - missing skills
    - assessment
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