import sqlite3

def conectar():
    return sqlite3.connect("livros.db")

def salvar_livro(livro):
    with conectar() as conn:
        conn.execute("""
            INSERT INTO livros (titulo, autor, preco, data_publicacao, descricao)
            VALUES (?, ?, ?, ?, ?)""",
            (livro.titulo, livro.autor, livro.preco, livro.data_publicacao, livro.descricao)
        )

def listar_livros(coluna):
    with conectar() as conn:
        return conn.execute("SELECT * FROM livros ORDER BY ? ASC", (coluna)).fetchall()

def buscar_por_id(id):
    with conectar() as conn:
        return conn.execute("SELECT * FROM livros WHERE id = ?", (id,)).fetchone()

def deletar_livro(id):
    with conectar() as conn:
        conn.execute("DELETE FROM livros WHERE id = ?", (id,))

def atualizar_livro(id, livro):
    with conectar() as conn:
        conn.execute("""
            UPDATE livros SET titulo=?, autor=?, preco=?, data_publicacao=?, descricao=?
            WHERE id=?""",
            (livro.titulo, livro.autor, livro.preco, livro.data_publicacao, livro.descricao, id)
        )

def buscar_por_titulo(titulo):
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM livros WHERE titulo LIKE ?",
            ('%' + titulo + '%',)
        ).fetchall()
        