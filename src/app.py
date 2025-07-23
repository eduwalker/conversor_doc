from flask import Flask, request, jsonify
from src.utils.autenticar import autenticar
from src.utils.downloader import baixar_arquivo
from src.utils.extractor import extrair_pdf, extrair_docx, extrair_excel
import os

app = Flask(__name__)


@app.route('/extrair-texto', methods=['POST'])
def extrair_texto():
    if not autenticar(request):
        return jsonify({"erro": "Não autorizado"}), 401

    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"erro": "URL não informada"}), 400

    try:
        arquivo = baixar_arquivo(url)
        if arquivo.endswith(".pdf"):
            texto = extrair_pdf(arquivo)
        elif arquivo.endswith(".docx"):
            texto = extrair_docx(arquivo)
        elif arquivo.endswith(".xlsx") or arquivo.endswith(".xls"):
            texto = extrair_excel(arquivo)
        else:
            return jsonify({"erro": "Formato de arquivo não suportado"}), 400
        os.remove(arquivo)
        return jsonify({"texto": texto.strip()})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
