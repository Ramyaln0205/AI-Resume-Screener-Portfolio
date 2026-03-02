import streamlit as st

st.title("AI Resume Screener")
st.write("Welcome to my AI Resume Screener App 🚀")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    