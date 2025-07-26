from models.livro import Livro
from repository import livro_repository

def test_salvar_e_listar(memory_db):
    livro = Livro("Titulo", "Autor", 10.0, "2020-01-01", "desc")
    livro_repository.salvar_livro(livro)
    livros = livro_repository.listar_livros()
    assert len(livros) == 1
    assert livros[0][1] == "Titulo"

def test_buscar_por_id(memory_db):
    livro = Livro("Titulo", "Autor", 10.0, "2020-01-01")
    livro_repository.salvar_livro(livro)
    encontrado = livro_repository.buscar_por_id(1)
    assert encontrado[1] == "Titulo"

def test_atualizar_livro(memory_db):
    livro = Livro("Original", "Autor", 10.0, "2020-01-01")
    livro_repository.salvar_livro(livro)
    atualizado = Livro("Novo", "Novo Autor", 20.0, "2021-01-01", "nova desc")
    livro_repository.atualizar_livro(1, atualizado)
    livro_editado = livro_repository.buscar_por_id(1)
    assert livro_editado[1] == "Novo"
    assert livro_editado[2] == "Novo Autor"

def test_deletar_livro(memory_db):
    livro = Livro("Titulo", "Autor", 10.0, "2020-01-01")
    livro_repository.salvar_livro(livro)
    livro_repository.deletar_livro(1)
    assert livro_repository.buscar_por_id(1) is None
