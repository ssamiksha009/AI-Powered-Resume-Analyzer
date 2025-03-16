import streamlit as st
from resume_parser import extract_text
from text_processing import clean_text
from similarity import calculate_similarity
from keyword_extraction import extract_keywords, get_skill_recommendations

st.title("📄 AI-Powered Resume Analyzer")

# Upload resume file
resume_file = st.file_uploader("📂 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Input job description
job_desc = st.text_area("📝 Paste Job Description Here")

if resume_file and job_desc:
    # Extract text from resume
    resume_text = extract_text(resume_file)
    
    # Clean and preprocess text
    cleaned_resume = clean_text(resume_text)
    cleaned_job_desc = clean_text(job_desc)

    # Compute similarity score
    similarity_score = calculate_similarity(cleaned_resume, cleaned_job_desc)

    # Extract keywords (skills) from job description
    job_keywords = extract_keywords(job_desc, max_keywords=10)
    resume_keywords = extract_keywords(resume_text, max_keywords=10)

    # Identify missing skills
    missing_skills = job_keywords - resume_keywords

    # Display match percentage
    st.subheader(f"✅ Match Percentage: {similarity_score}%")

    if similarity_score > 75:
        st.success("🔥 Great match! The resume fits the job description well.")
    elif similarity_score > 50:
        st.warning("⚡ Moderate match. Consider adding relevant skills.")
    else:
        st.error("🚨 Low match. The resume may not be suitable for this job.")

    # Display missing skills
    if missing_skills:
        st.subheader("🔍 Missing Skills:")
        st.write(", ".join(missing_skills))

        # Provide skill improvement recommendations
        recommendations = get_skill_recommendations(missing_skills)
        
        if recommendations:
            st.subheader("📌 Recommended Learning Resources:")
            for rec in recommendations:
                st.markdown(rec)
