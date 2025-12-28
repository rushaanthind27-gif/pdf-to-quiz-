import streamlit as st
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import random
from sklearn.feature_extraction.text import TfidfVectorizer

# ---------------------------
# PDF TEXT EXTRACTION
# ---------------------------

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text


# ---------------------------
# SIMPLE QUESTION GENERATORS
# ---------------------------

def generate_short_questions(text, num_q=5):
    sentences = sent_tokenize(text)

    if len(sentences) == 0:
        return []

    random.shuffle(sentences)
    questions = []

    for sent in sentences[:num_q]:
        questions.append(sent.replace(".", "?"))

    return questions


def generate_fill_in_the_blank(text, num_q=5):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)

    content_words = [w for w in words if w.isalpha() and w.lower() not in stop_words]

    if len(content_words) < num_q:
        num_q = len(content_words)

    random.shuffle(content_words)

    questions = []

    for i in range(num_q):
        target = content_words[i]
        blank_text = text.replace(target, "______", 1)
        questions.append((blank_text[:200] + "...", target))

    return questions


def generate_mcq(text, num_q=5):
    sentences = sent_tokenize(text)

    if len(sentences) < 5:
        return []

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(sentences)

    feature_names = vectorizer.get_feature_names_out()
    questions = []

    for i in range(min(num_q, len(sentences))):
        sentence = sentences[i]
        tfidf_scores = X[i].toarray()[0]

        top_indices = tfidf_scores.argsort()[-4:]
        options = [feature_names[j] for j in top_indices]

        correct = options[-1]
        random.shuffle(options)

        questions.append({
            "question": f"What is the key term in: '{sentence[:120]}...'",
            "options": options,
            "answer": correct
        })

    return questions


# ---------------------------
# STREAMLIT APP
# ---------------------------

st.set_page_config(page_title="PDF → Quiz Generator", layout="centered")
st.title("📚 PDF to Quiz Generator")
st.write("Upload a PDF and generate quizzes automatically.")


uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)

    st.success("Text extracted!")

    if len(text) < 200:
        st.warning("PDF text seems too short to generate questions.")
    else:
        st.subheader("📝 Short-Answer Questions")
        short_qs = generate_short_questions(text, 5)
        for i, q in enumerate(short_qs, 1):
            st.write(f"**Q{i}. {q}**")

        st.subheader("✍️ Fill in the Blanks")
        fib = generate_fill_in_the_blank(text, 5)
        for i, (q, ans) in enumerate(fib, 1):
            st.write(f"**Q{i}. {q}**")
            st.write(f"✔️ Answer: `{ans}`")

        st.subheader("❓ Multiple Choice Questions")
        mcqs = generate_mcq(text, 5)

        for i, mcq in enumerate(mcqs, 1):
            st.write(f"**Q{i}. {mcq['question']}**")
            for opt in mcq["options"]:
                st.write(f"- {opt}")
            st.write(f"✔️ Correct Answer: `{mcq['answer']}`")
