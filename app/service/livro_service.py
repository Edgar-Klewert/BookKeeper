from models.livro import Livro
import repository.livro_repository as repo

def criar_livro(dados):
    livro = Livro(**dados)
    repo.salvar_livro(livro)

def listar_livros(coluna):
    return repo.listar_livros(coluna)

def buscar_livro(id):
    return repo.buscar_por_id(id)

def remover_livro(id):
    repo.deletar_livro(id)

def editar_livro(id, dados):
    livro = Livro(**dados)
    repo.atualizar_livro(id, livro)

def buscar_livro_por_titulo(titulo):
    return repo.buscar_por_titulo(titulo)