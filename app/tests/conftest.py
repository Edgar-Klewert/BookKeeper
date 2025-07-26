import pytest
import sqlite3
from repository import livro_repository

@pytest.fixture
def memory_db(monkeypatch):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        preco REAL NOT NULL,
        data_publicacao TEXT NOT NULL,
        descricao TEXT
    )
    """)
    conn.commit()

    # Monkeypatch para forçar o repositório a usar o banco em memória
    monkeypatch.setattr(livro_repository, "conectar", lambda: conn)
    return conn
