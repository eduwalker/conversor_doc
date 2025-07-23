# Conversor API

API em Python para extração de texto de arquivos PDF, DOCX e Excel (.xlsx), com autenticação via token e preparada para rodar em ambientes Docker Swarm com integração direta ao n8n.

---

## ✨ Funcionalidades

- 🔍 Extração de texto de:
    - PDFs
    - Arquivos Word (.docx)
    - Planilhas Excel (.xlsx e .xls)
- 🔒 Autenticação via Bearer Token
- ⚙️ Compatível com deploy em Docker Swarm
- 🤝 Integração fácil com o n8n via rede interna

---

## 📦 Requisitos

- Python 3.10+
- Docker (para uso em produção)
- `.env` com token de autenticação (modelo abaixo)

---

## 📁 Estrutura

.
├── src/
│ ├── app.py # Roteamento da API
│ ├── config.py # Carrega variáveis de ambiente
│ └── utils/
│ ├── autenticar.py # Função de autenticação por token
│ ├── downloader.py # Faz download do arquivo a partir de URL
│ └── extractor.py # Extrai texto de PDF, DOCX, XLSX
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md

yaml
Copiar
Editar

---

## 🚀 Como rodar localmente

### 1. Crie seu `.env`

```env
TOKEN_API_CONVERSAO=seu-token-seguro-aqui
2. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
3. Rode a API
bash
Copiar
Editar
python src/app.py
A API estará disponível em: http://localhost:5002/extrair-texto

🐳 Como rodar com Docker
bash
Copiar
Editar
docker build -t conversor-api .
docker run -p 5002:5002 --env-file .env conversor-api
🧩 Endpoint principal
POST /extrair-texto
Headers
pgsql
Copiar
Editar
Authorization: Bearer seu-token
Content-Type: application/json
Body
json
Copiar
Editar
{
  "url": "https://exemplo.com/arquivo.docx"
}
Resposta
json
Copiar
Editar
{
  "texto": "Conteúdo extraído aqui..."
}
🔐 Segurança
A API exige um token de autenticação via header Authorization. O token deve ser configurado via variável de ambiente TOKEN_API_CONVERSAO.

🛠️ Deploy via Docker Swarm
bash
Copiar
Editar
docker stack deploy -c docker-compose.yml conversorapi
Certifique-se de estar na mesma rede interna que o n8n (ex: n8n-internal) e que o .env esteja presente no servidor.

📄 Licença
MIT - 2025 © AllTank

yaml
Copiar
Editar

---

Se quiser posso personalizar mais com seu nome, link da empresa ou incluir instruções específicas do n8n também. 