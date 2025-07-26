from service import livro_service
from models.livro import Livro

def test_criar_listar_livro(memory_db):
    dados = {"titulo": "Teste", "autor": "Autor", "preco": 12.0, "data_publicacao": "2020-01-01"}
    livro_service.criar_livro(dados)
    livros = livro_service.listar_livros()
    assert len(livros) == 1
    assert livros[0][1] == "Teste"

def test_buscar_e_remover(memory_db):
    dados = {"titulo": "Teste", "autor": "Autor", "preco": 12.0, "data_publicacao": "2020-01-01"}
    livro_service.criar_livro(dados)
    livro = livro_service.buscar_livro(1)
    assert livro[1] == "Teste"
    livro_service.remover_livro(1)
    assert livro_service.buscar_livro(1) is None

def test_editar_livro(memory_db):
    dados = {"titulo": "Antigo", "autor": "Autor", "preco": 12.0, "data_publicacao": "2020-01-01"}
    livro_service.criar_livro(dados)
    novos_dados = {"titulo": "Novo", "autor": "Autor2", "preco": 20.0, "data_publicacao": "2021-01-01"}
    livro_service.editar_livro(1, novos_dados)
    livro = livro_service.buscar_livro(1)
    assert livro[1] == "Novo"
    assert livro[2] == "Autor2"
