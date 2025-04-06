import streamlit as st
from resume_parser import parse_resume, match_resume
import os

st.set_page_config(page_title="AI Resume Screener", layout="centered")

st.title("📄 AI-Powered Resume Screener")
st.write("Upload a resume and see how well it matches the job description!")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    with open(f"temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("Resume uploaded!")

    with open("job_description.txt", "r") as jd_file:
        job_description = jd_file.read()

    resume_text = parse_resume("temp_resume.pdf")
    match_score, keywords = match_resume(resume_text, job_description)

    st.subheader("✅ Match Score:")
    st.progress(match_score)

    st.markdown(f"**Extracted Skills/Keywords:**")
    st.code(", ".join(keywords))

    os.remove("temp_resume.pdf")
