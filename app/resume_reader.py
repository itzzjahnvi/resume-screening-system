import re
import pdfplumber
from docx import Document

def extract_text(file_path):
    text = ""

    try:
        if file_path.lower().endswith(".pdf"):
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + " "

        elif file_path.lower().endswith(".docx"):
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + " "

        elif file_path.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read() + " "

        else:
            print(f"Unsupported file type: {file_path}")
            return ""

    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return ""

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text 