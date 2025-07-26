import pytest
from main import listar, adicionar, buscar, editar, deletar

def test_listar_vazio(monkeypatch, capsys):
    monkeypatch.setattr("service.livro_service.listar_livros", lambda: [])
    listar()
    captured = capsys.readouterr()
    assert "Nenhum livro encontrado" in captured.out

def test_buscar_nao_encontrado(monkeypatch, capsys):
    monkeypatch.setattr("service.livro_service.buscar_livro", lambda id: None)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    buscar()
    captured = capsys.readouterr()
    assert "Livro não encontrado" in captured.out

def test_adicionar(monkeypatch, capsys):
    # Simula entradas do prompt
    inputs = iter(["Livro Teste", "Autor Teste", "10.0", "2020-01-01", "desc"])
    monkeypatch.setattr("typer.prompt", lambda msg, default=None: next(inputs))
    monkeypatch.setattr("service.livro_service.criar_livro", lambda dados: None)
    adicionar()
    captured = capsys.readouterr()
    assert "Livro cadastrado" in captured.out

def test_editar(monkeypatch, capsys):
    inputs = iter(["1", "Novo Titulo", "Novo Autor", "20.0", "2022-01-01", "desc nova"])
    monkeypatch.setattr("typer.prompt", lambda msg, default=None: next(inputs))
    monkeypatch.setattr("service.livro_service.buscar_livro", lambda id: (1, "Antigo", "Autor", 10.0, "2020-01-01", "old desc"))
    monkeypatch.setattr("service.livro_service.editar_livro", lambda id, dados: None)
    editar()
    captured = capsys.readouterr()
    assert "Livro atualizado" in captured.out

def test_deletar(monkeypatch, capsys):
    monkeypatch.setattr("typer.prompt", lambda msg: "1")
    monkeypatch.setattr("service.livro_service.remover_livro", lambda id: None)
    deletar()
    captured = capsys.readouterr()
    assert "Livro deletado" in captured.out
