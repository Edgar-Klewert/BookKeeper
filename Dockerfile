# Dockerfile

FROM python:3.11-slim

# Diretório de trabalho na imagem
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto
COPY . .

# Definir o diretório de trabalho como app/
WORKDIR /app/app

# Rodar como módulo garante que encontre 'app' como pacote
CMD ["python", "-m", "main"]
