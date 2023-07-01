import io
from reportlab.pdfgen import canvas

def create_latex_file() -> bytes:
    latex_content = "\\documentclass{article}\n\\begin{document}\nThis is the content of the LaTeX file.\n\\end{document}"
    file_obj = io.BytesIO()
    file_obj.write(latex_content.encode())
    file_obj.seek(0)
    return file_obj

def create_pdf_file():
    file_obj = io.BytesIO()
    p = canvas.Canvas(file_obj)

    # Add content to the PDF
    p.drawString(100, 100, "This is the content of the PDF file.")
    
    p.showPage()
    p.save()
    file_obj.seek(0)

    return file_obj