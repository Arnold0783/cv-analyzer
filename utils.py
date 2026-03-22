import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """
    Extract text from uploaded PDF.
    """
    text = ""
    try:
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf:
            text += page.get_text()
    except Exception as e:
        print("PDF extraction error:", e)
    return text