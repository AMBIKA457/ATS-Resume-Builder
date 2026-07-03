import streamlit as st
from ai_resume import generate_resume
from ats_score import calculate_ats_score
from pdf_generator import create_pdf

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AI ATS Resume Builder",
    page_icon="📄",
    layout="wide"
)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.title("📄 AI ATS Resume Builder")
    st.markdown("---")
    st.write("### Features")
    st.write("✅ AI Resume Generation")
    st.write("✅ ATS Score")
    st.write("✅ Missing Keywords")
    st.write("✅ PDF Download")
    st.write("✅ Job Matching")

# -------------------------
# Main Title
# -------------------------
st.title("📄 AI ATS Resume Builder")
st.write("Generate professional ATS-friendly resumes using AI.")

# -------------------------
# Personal Details
# -------------------------
st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

with col2:
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")
    address = st.text_area("Address")

# -------------------------
# Professional Summary
# -------------------------
summary = st.text_area(
    "Professional Summary",
    placeholder="Write a short summary about yourself."
)

# -------------------------
# Skills
# -------------------------
skills = st.text_area(
    "Skills",
    placeholder="Python, FastAPI, AWS, Docker, SQL"
)

# -------------------------
# Experience
# -------------------------
experience = st.text_area(
    "Experience",
    placeholder="Describe your work experience."
)

# -------------------------
# Education
# -------------------------
education = st.text_area(
    "Education",
    placeholder="""
B.Tech Information Technology
ABC University
2025
"""
)

# -------------------------
# Projects
# -------------------------
projects = st.text_area(
    "Projects",
    placeholder="AI ATS Resume Builder"
)

# -------------------------
# Certifications
# -------------------------
certifications = st.text_area(
    "Certifications",
    placeholder="Generative AI Certification"
)

# -------------------------
# Job Description
# -------------------------
job_description = st.text_area(
    "Paste Job Description",
    placeholder="Python, FastAPI, Docker, AWS, REST API"
)

# -------------------------
# Generate Button
# -------------------------
if st.button("🚀 Generate Resume"):

    if not name:
        st.warning("Please enter your name.")
        st.stop()

    with st.spinner("Generating Resume..."):

        resume = generate_resume(
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
        )

    # ATS Score
    score, missing = calculate_ats_score(
        resume,
        job_description
    )

    # Create PDF
    pdf_file = create_pdf(
        name,
        resume
    )

    st.success("✅ Resume Generated Successfully!")

    # Resume Output
    st.subheader("📄 Generated Resume")

    st.text_area(
        "Resume",
        resume,
        height=500
    )

    # ATS Score
    st.subheader("📊 ATS Score")

    st.progress(score / 100)

    if score >= 80:
        st.success(f"ATS Score: {score}%")
    elif score >= 60:
        st.warning(f"ATS Score: {score}%")
    else:
        st.error(f"ATS Score: {score}%")

    # Missing Keywords
    st.subheader("❌ Missing Keywords")

    if missing:
        for keyword in missing:
            st.write(f"• {keyword}")
    else:
        st.success("✅ No missing keywords found.")

    # Download PDF
    st.subheader("📥 Download Resume")

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download PDF",
            data=file,
            file_name="ATS_Resume.pdf",
            mime="application/pdf"
        )