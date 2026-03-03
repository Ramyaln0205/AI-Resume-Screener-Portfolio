import streamlit as st
import PyPDF2
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screener")
st.write("Welcome to my AI Resume Screener App 🚀")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

# Paste job description
job_description = st.text_area("Paste Job Description here:")

if uploaded_file is not None and job_description:
    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    # Compare Resume and JD
    texts = [resume_text, job_description]
    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    
    match_score = round(cosine_sim[0][1] * 100, 2)
    
    st.success(f"Resume Match Score: {match_score}%")
    

    