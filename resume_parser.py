import pdfplumber
import docx2txt
from io import BytesIO

def extract_text(uploaded_file):
    """Extracts text from an uploaded resume file (PDF or DOCX)"""
    
    file_extension = uploaded_file.name.split(".")[-1].lower()

    if file_extension == "pdf":
        with pdfplumber.open(BytesIO(uploaded_file.read())) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_extension == "docx":
        text = docx2txt.process(uploaded_file)
    else:
        text = ""

    return text.strip()
