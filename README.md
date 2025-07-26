# 📚 BookKeeper

Um sistema simples em Python para cadastro e gerenciamento de livros, usando linha de comando interativa (CLI) com **Typer** + **Rich** e banco de dados **SQLite**.  
Projeto organizado em camadas (`service`, `repository`, `models`) e preparado para execução local, testes unitários e contêiner Docker.

---

## ✨ Funcionalidades

- 📄 Listar livros  
- ➕ Adicionar novos livros  
- 🔍 Buscar livro por ID  
- ✏️ Editar livro existente  
- 🗑️ Deletar livro  
- 📦 Estrutura limpa e modular  
- 🧪 Testes unitários  
- 🐳 Docker & Docker Compose  

---

## ⚙️ Requisitos

- Python **3.10+**
- Docker (opcional)
- Git

---

## 🛠️ Instalação local

```bash
# Clone o repositório
git clone https://github.com/Edgar-Klewert/BookKeeper.git
cd BookKeeper

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### ▶️ Como executar

```bash
cd app
python main.py
```

A interface interativa vai abrir no terminal para você gerenciar os livros.

---

## 🐳 Executar com Docker

### Build da imagem:

```bash
docker build -t bookkeeper-app .
```

### Rodar o contêiner:

```bash
docker run -it bookkeeper-app
```

### Ou, usando docker-compose:

```bash
docker-compose up --build
```

---

## ✅ Rodar testes

### Usando o Pytest diretamente:

```bash
pytest
```

### Ou usando Makefile (se preferir):

```bash
make test
```

---

## 📦 Dependências principais

- `typer[all]` → CLI interativa  
- `rich` → Tabelas e cores no terminal  
- `pytest` → Testes unitários  
- `sqlite3`, `logging`, `datetime` → Módulos padrão do Python  

---

## 📌 Observações

- Os dados ficam salvos no arquivo `livros.db` (SQLite).
- Logs são gravados em `logs/app.log`.
