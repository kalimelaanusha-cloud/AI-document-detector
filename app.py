import streamlit as st
from pathlib import Path

from document_loader import extract_text
from detector import create_embedding
from database import add_document
from ai_analyzer import analyze_document


st.set_page_config(
    page_title="AI Document Detector",
    page_icon="📄",
    layout="centered"
)

st.markdown("""
<style>

.stApp {
    background-color: #F5F0E6;
    color: #000000;
}

.main-title {
    text-align: center;
    color: #6B8068;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #000000;
    font-size: 17px;
    margin-bottom: 30px;
}

.upload-box {
    background-color: #E3EBDD;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #A8B89F;
    margin-bottom: 20px;
    color: #000000;
}

.section-title {
    color: #6B8068;
    font-size: 24px;
    font-weight: 600;
}

.result-box {
    background-color: #E3EBDD;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #82977D;
    margin-top: 20px;
    color: #000000;
}

.stTextArea textarea {
    color: #000000 !important;
    background-color: #FFFFFF !important;
}

.stTextInput input {
    color: #000000 !important;
}

.stFileUploader {
    color: #000000;
}

.stButton > button {
    background-color: #82977D;
    color: #FFFFFF;
    border-radius: 10px;
    border: none;
    padding: 10px 25px;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #6B8068;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">📄 AI Document Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload a document and analyze it using AI</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="upload-box">',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "📁 Upload your document",
    type=["pdf", "docx", "xlsx"]
)

st.markdown("</div>", unsafe_allow_html=True)


if uploaded_file is not None:

    st.success(f"File uploaded: {uploaded_file.name}")

    file_path = Path("documents") / uploaded_file.name
    file_path.parent.mkdir(exist_ok=True)

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    if st.button("🔍 Analyze Document"):

        try:

            with st.spinner("📖 Reading document..."):
                text = extract_text(str(file_path))

            if not text.strip():
                st.error("No text could be extracted from this document.")
                st.stop()

            st.markdown(
                '<div class="section-title">📄 Extracted Text</div>',
                unsafe_allow_html=True
            )

            st.text_area(
                "Document content",
                text,
                height=250
            )

            with st.spinner("🧠 Creating document embedding..."):
                embedding = create_embedding(text)

            add_document(
                uploaded_file.name,
                text,
                embedding
            )

            st.success("✅ Document stored successfully!")

            with st.spinner("🤖 AI is analyzing the document..."):
                result = analyze_document(text)

            st.markdown(
                '<div class="section-title">🤖 AI Analysis</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="result-box">{result}</div>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")