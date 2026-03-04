# AI-Resume-Screener-Portfolio# 🚀 AI Resume Screener

An AI-powered Resume Screening Web Application built using Streamlit and Machine Learning.

## 📌 Project Overview

The AI Resume Screener analyzes a candidate's resume against a job description and calculates a match score using Natural Language Processing (NLP) techniques.

It highlights:
- ✅ Matched Skills (Green)
- ❌ Missing Skills (Red)
- 📊 Resume Match Percentage

## 🛠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- PyPDF2
- NLP (CountVectorizer & Cosine Similarity)

## ⚙️ Features

- Upload Resume (PDF)
- Paste Job Description
- Automatic Skill Extraction
- Resume Matching Score
- Highlighted Skill Analysis
- Clean & Interactive UI

## 🧠 How It Works

1. Extracts text from uploaded resume (PDF).
2. Converts resume & job description into numerical vectors.
3. Uses Cosine Similarity to calculate match percentage.
4. Identifies matched and missing skills.
5. Displays skill comparison visually.

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py