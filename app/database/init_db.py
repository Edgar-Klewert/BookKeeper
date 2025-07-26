import sqlite3
import os

DADOS_INICIAIS = [
    ("A Guerra dos Tronos", "George R. R. Martin", 89.90, "1996-08-06", "As Crônicas de Gelo e Fogo"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 39.90, "1997-06-26", "Primeiro livro da saga Harry Potter"),
    ("O Hobbit", "J.R.R. Tolkien", 35.00, "1937-09-21", "A jornada de Bilbo"),
    ("1984", "George Orwell", 39.90, "1949-06-08", "Distopia totalitária"),
]

def inicializar_banco():
    novo = not os.path.exists("livros.db")

    conn = sqlite3.connect("livros.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        preco REAL NOT NULL,
        data_publicacao TEXT NOT NULL,
        descricao TEXT
    )
    """)

    if novo:
        cursor.executemany("""
            INSERT INTO livros (titulo, autor, preco, data_publicacao, descricao)
            VALUES (?, ?, ?, ?, ?)""", DADOS_INICIAIS)
        conn.commit()

    conn.close()
