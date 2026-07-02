import streamlit as st
from ai_resume import generate_resume

st.set_page_config(
    page_title="AI ATS Resume Builder",
    page_icon="📄"
)

st.title("📄 AI ATS Resume Builder")

name = st.text_input("Full Name")

skills = st.text_area("Skills")

experience = st.text_area("Experience")

if st.button("Generate Resume"):

    with st.spinner("Generating Resume..."):
        resume = generate_resume(
            name,
            skills,
            experience
        )

    st.success("Resume Generated!")

    st.write(resume)