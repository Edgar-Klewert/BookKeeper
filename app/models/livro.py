from datetime import datetime

class Livro:
    def __init__(self, titulo, autor, preco, data_publicacao, descricao=None, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.data_publicacao = data_publicacao
        self.descricao = descricao
        self.validar()

    def validar(self):
        if not self.titulo.strip():
            raise ValueError("Título é obrigatório")
        if not self.autor.strip():
            raise ValueError("Autor é obrigatório")
        if self.preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
        try:
            datetime.strptime(self.data_publicacao, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Data inválida (use YYYY-MM-DD)")
