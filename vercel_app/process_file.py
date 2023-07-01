import io

def create_latex_file() -> bytes:
    latex_content = "\\documentclass{article}\n\\begin{document}\nThis is the content of the LaTeX file.\n\\end{document}"
    file_obj = io.BytesIO()
    file_obj.write(latex_content.encode())
    file_obj.seek(0)
    return file_obj