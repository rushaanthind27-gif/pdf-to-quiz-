# PDF to Quiz Generator 🎓

Convert any PDF (notes, textbook, document) into:

- Multiple-choice questions  
- Short-answer questions  
- Fill-in-the-blank questions  

Built for hackathons and students to revise faster and generate quizzes automatically.

---

## 🚀 Features

- Upload any PDF
- Automatically generates quizzes
- Extracts key terms and topics
- MCQs, short questions, fill-in-the-blanks
- Runs locally on your computer
- 100% Python + Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- NLTK
- Scikit-learn
- PyPDF2

---

## ✅ Installation Guide (Step-by-Step)

### 1) Install Python

Download from:
https://www.python.org/downloads/

IMPORTANT: During installation tick:
Add Python to PATH

---

### 2) Open Command Prompt

Windows:
Press Windows Key → type cmd → press Enter

---

### 3) Install required libraries

Run:

python -m pip install streamlit PyPDF2 nltk scikit-learn

---

### 4) Download NLTK data

Run:

python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"

---

### 5) Download or clone this project

Either:
- Download ZIP and extract
or
- Clone repository

---

### 6) Run the app 🚀

In Command Prompt go to the project folder, e.g.:

cd Desktop\pdf-to-quiz-app

Then run:

python -m streamlit run pdf_to_quiz_app.py

The app will open in your browser automatically.

---

## 🧑‍🏫 How to Use

1. Click Upload PDF
2. Select any PDF file
3. Wait for extraction
4. View generated questions:
   - MCQs
   - Short-answer questions
   - Fill-in-the-blanks

---

## ⚠️ Common Errors & Fixes

Streamlit not recognized:
python -m pip install streamlit

No module named nltk:
python -m pip install nltk

LookupError: punkt or punkt_tab:
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords')"

---

## ⭐ Future Improvements

- Export quiz as PDF or Word
- Difficulty levels
- Answer key export
- Support for scanned PDFs (OCR)
- Web deployment version

---

## 🏆 Hackathon Theme Suggestions

- EdTech
- AI for Learning
- Productivity tools
- Accessibility in education
