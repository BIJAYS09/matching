from openai import OpenAI

from app.core.config import settings

from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file  

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
    
    messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    response = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3, max_tokens=1000).invoke(messages)

    print("Semantic Match Analysis Response:", response.text.strip())
    return response.text.strip()