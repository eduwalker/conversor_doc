import pdfplumber
import pandas as pd
import docx


def extrair_pdf(caminho):
    with pdfplumber.open(caminho) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)


def extrair_docx(caminho):
    doc = docx.Document(caminho)
    return "\n".join([p.text for p in doc.paragraphs])


def extrair_excel(caminho):
    df = pd.read_excel(caminho, sheet_name=None)
    texto = ""
    for nome_aba, tabela in df.items():
        texto += f"\n--- {nome_aba} ---\n"
        texto += tabela.to_string(index=False)
    return texto
