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
````

----
## 2. Instale as dependências
   ````bash
   pip install -r requirements.txt
   ````
----
## 3. Rode a API
   python src/app.py

   A API estará disponível em:
   ````
   http://localhost:5002/extrair-texto
   ````
----

## 🧩 Endpoint principal

### `POST /extrair-texto`

#### 🔑 Headers
```http
Authorization: Bearer seu-token
Content-Type: application/json
````
#### 📦 Body
```body
{
  "url": "https://exemplo.com/arquivo.docx"
}
````
#### 🔁 Response
````response
{
  "texto": "Conteúdo extraído aqui..."
}
````


## 🔐 Segurança
A API exige um token de autenticação via header Authorization. O token deve ser configurado via variável de ambiente 
````
TOKEN_API_CONVERSAO
````
---
## 📄 Licença

Este projeto é licenciado sob os termos da licença MIT.

Distribuído com amor por **Eduardo Oliveira** – 2025  
Todos os direitos reservados.
