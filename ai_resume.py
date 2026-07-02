from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_resume(name, skills, experience):

    prompt = f"""
    Create an ATS-friendly resume.

    Name: {name}

    Skills:
    {skills}

    Experience:
    {experience}

    Make it professional and ATS optimized.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content