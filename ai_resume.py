from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_resume(
    name,
    phone,
    email,
    address,
    linkedin,
    github,
    summary,
    skills,
    experience,
    education,
    projects,
    certifications
):

    prompt = f"""
Create a professional ATS-friendly resume.

Personal Information:
Name: {name}
Phone: {phone}
Email: {email}
Address: {address}
LinkedIn: {linkedin}
GitHub: {github}

Professional Summary:
{summary}

Skills:
{skills}

Experience:
{experience}

Education:
{education}

Projects:
{projects}

Certifications:
{certifications}

Instructions:
- Create an ATS-friendly resume.
- Use proper section headings.
- Improve the summary professionally.
- Enhance experience points with action verbs.
- Optimize skills for ATS keywords.
- Return only the resume.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert ATS resume writer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=2000
    )

    return response.choices[0].message.content