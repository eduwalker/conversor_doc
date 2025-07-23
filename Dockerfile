FROM python:3.11-slim

WORKDIR /app

# Copia código-fonte e dependências
COPY ./src /app/src
COPY requirements.txt /app/

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define variáveis de ambiente (via Docker Swarm ou .env no host)
ENV PYTHONPATH=/app

# Comando de inicialização
CMD ["python", "src/app.py"]
