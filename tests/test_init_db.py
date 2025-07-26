import sqlite3
import os
import pytest
from database import init_db

def test_inicializar_banco(tmp_path):
    db_path = tmp_path / "test.db"
    # Monkeypatch o caminho do banco
    original_path = os.path.exists
    os.path.exists = lambda path: False  # força ser novo

    # Copia função e substitui caminho dentro dela
    old_connect = sqlite3.connect
    sqlite3.connect = lambda _: old_connect(db_path)

    try:
        init_db.inicializar_banco()
        assert db_path.exists()
        conn = sqlite3.connect(db_path)
        cursor = conn.execute("SELECT count(*) FROM livros")
        total = cursor.fetchone()[0]
        assert total >= 1 
        conn.close()
    finally:
        # Restaura
        os.path.exists = original_path
        sqlite3.connect = old_connect
