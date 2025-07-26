import pytest
from models.livro import Livro

def test_livro_valido():
    livro = Livro(
        titulo="1984",
        autor="George Orwell",
        preco=39.90,
        data_publicacao="1949-06-08",
        descricao="Distopia"
    )
    assert livro.titulo == "1984"

def test_titulo_obrigatorio():
    with pytest.raises(ValueError, match="Título é obrigatório"):
        Livro("", "Autor", 10, "2020-01-01")

def test_autor_obrigatorio():
    with pytest.raises(ValueError, match="Autor é obrigatório"):
        Livro("Titulo", "", 10, "2020-01-01")

def test_preco_maior_que_zero():
    with pytest.raises(ValueError, match="Preço deve ser maior que zero"):
        Livro("Titulo", "Autor", 0, "2020-01-01")

def test_data_invalida():
    with pytest.raises(ValueError, match="Data inválida"):
        Livro("Titulo", "Autor", 10, "31-12-2020")
