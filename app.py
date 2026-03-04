import streamlit as st
import PyPDF2
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screener", layout="centered")
st.title("AI Resume Screener 🚀")
st.write("Upload your resume and paste a job description to get a match score.")

# Upload Resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Job Description Input
job_description = st.text_area(
    "Paste Job Description here:",
    height=300
)

def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def get_skills(text):
    skills_list = ["python", "machine learning", "nlp", "tensorflow", "pytorch", 
                   "scikit-learn", "data analysis", "sql", "pandas", 
                   "numpy", "spacy", "keras", "statistics"]

    text_lower = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill)

    return found_skills

if uploaded_file is not None and job_description:
    resume_text = extract_text(uploaded_file)
    
    # Compute match score
    texts = [resume_text, job_description]
    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    match_score = round(cosine_sim[0][1] * 100, 2)
    
    st.success(f"Resume Match Score: {match_score}%")

    # Highlight skills
    resume_skills = set(get_skills(resume_text))
    jd_skills = set(get_skills(job_description))
    
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills
    
    if matched_skills:
        st.markdown("**Matched Skills:** " + ", ".join([f"<span style='color:green'>{skill}</span>" for skill in matched_skills]), unsafe_allow_html=True)
    if missing_skills:
        st.markdown("**Missing Skills:** " + ", ".join([f"<span style='color:red'>{skill}</span>" for skill in missing_skills]), unsafe_allow_html=True)