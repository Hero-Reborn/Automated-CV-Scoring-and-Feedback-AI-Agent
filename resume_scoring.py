from docx import Document
from PyPDF2 import PdfReader

def extract_text_from_docx(docx_file):
    document = Document(docx_file)
    text = ''
    for para in document.paragraphs:
        text += para.text + '\n'
    return text

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def score_resume(resume_text):
    score = 0
    
    keywords = ["Python", "Machine Learning", "Data Science", "AI", "Deep Learning"]
    for keyword in keywords:
        score += resume_text.lower().count(keyword.lower()) * 2  
    if "years of experience" in resume_text.lower():
        score += 5  
    if "Master" in resume_text or "PhD" in resume_text:
        score += 10 
    return score

def process_resume(file_path):
    if file_path.endswith('.docx'):
        resume_text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(file_path)
    
    score = score_resume(resume_text)
    return score