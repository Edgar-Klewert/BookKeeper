import typer
from rich.console import Console
from rich.table import Table
from database.init_db import inicializar_banco
import service.livro_service as service
from utils.logger import logger

app = typer.Typer()
console = Console()

def obter_id_valido(mensagem: str) -> int:
    entrada = typer.prompt(mensagem)
    if not entrada.isdigit():
        raise ValueError("O ID deve ser um número inteiro positivo.")
    id = int(entrada)
    if not service.buscar_livro(id):
        raise ValueError(f"Nenhum livro encontrado com ID {id}.")
    return id

def obter_preco_valido(default: str = None) -> float:
    while True:
        prompt_msg = "Preço (ex: 35.00 ou 35,00)" if not default else f"Novo Preço (padrão: {default})"
        entrada = typer.prompt(prompt_msg, default=default).strip().replace(",", ".")
        try:
            preco = float(entrada)
            if preco <= 0:
                raise ValueError
            return preco
        except ValueError:
            console.print("[yellow]⚠ Insira um número válido e positivo para o preço.[/yellow]")

def listar():
    logger.info("Listando livros")
    console.print("como deseja listae os livros?")
    console.print("1. Por Título")
    console.print("2. Por ID")
    escolha_order = typer.prompt("Escolha uma opção (1 ou 2)", default="1")
    
    if escolha_order == "1":
        coluna = "titulo"
    else:
        coluna = "id"
        
    livros = service.listar_livros(coluna)
    
    if not livros:
        console.print("[yellow]Nenhum livro encontrado.[/yellow]")
        return
    tabela = Table(title="📚 Lista de Livros")
    tabela.add_column("ID", style="cyan")
    tabela.add_column("Título")
    tabela.add_column("Autor")
    tabela.add_column("Preço", justify="right")
    tabela.add_column("Data", justify="center")
    tabela.add_column("Descrição")
    for l in livros:
        tabela.add_row(str(l[0]), l[1], l[2], f"R${l[3]:.2f}", l[4], l[5] or "-")
    console.print(tabela)

def adicionar():
    try:
        logger.info("Iniciando cadastro de livro")
        titulo = typer.prompt("Título")
        autor = typer.prompt("Autor (opcional)", default="")
        preco = obter_preco_valido()
        data_publicacao = typer.prompt("Data de Publicação (YYYY-MM-DD)")
        descricao = typer.prompt("Descrição (opcional)", default="")
        dados = {
            "titulo": titulo,
            "autor": autor,
            "preco": preco,
            "data_publicacao": data_publicacao,
            "descricao": descricao
        }
        service.criar_livro(dados)
        logger.info(f"Livro cadastrado: {titulo} por {autor}")
        console.print("[green]✅ Livro cadastrado com sucesso![/green]")
    except Exception as e:
        logger.error(f"Erro ao cadastrar livro: {e}")
        console.print(f"[red]Erro:[/red] {e}")

def deletar():
    try:
        id = obter_id_valido("ID do livro para deletar")
        service.remover_livro(id)
        
        console.print(f"[cyan] deseja realmente deletar o livro com ID {id}?[/cyan]")
        
        confirmar = typer.confirm("Confirma a exclusão?")
        if not confirmar:
            console.print("[yellow]Exclusão cancelada.[/yellow]")
            logger.info("Exclusão de livro cancelada pelo usuário")
            return
                    
        logger.info(f"Livro deletado (ID: {id})")
        console.print("[green]✅ Livro deletado.[/green]")
    except Exception as e:
        logger.error(f"Erro ao deletar livro: {e}")
        console.print(f"[red]Erro:[/red] {e}")
        
def buscar_por_titulo():
    try:
        titulo = typer.prompt("Título do livro para buscar")
        livro = service.buscar_livro_por_titulo(titulo)
        if not livro:
            console.print("[yellow]Nenhum livro encontrado com esse título.[/yellow]")
            return 
        
        logger.info(f"Livro encontrado pelo título: {titulo}")
        console.print(f"[cyan]ID:[/cyan] {livro[0]}")
        console.print(f"[cyan]Título:[/cyan] {livro[1]}")
        console.print(f"[cyan]Autor:[/cyan] {livro[2]}")
        console.print(f"[cyan]Preço:[/cyan] R${livro[3]:.2f}")
        console.print(f"[cyan]Data:[/cyan] {livro[4]}")
        console.print(f"[cyan]Descrição:[/cyan] {livro[5] or '-'}")
        
    except Exception as e:
        logger.error(f"Erro ao buscar livro por título: {e}")
        console.print(f"[red]Erro:[/red] {e}")
        
def editar():
    try:
        id = obter_id_valido("ID do livro para editar")
        livro_original = service.buscar_livro(id)
        titulo = typer.prompt("Novo Título", default=livro_original[1])
        autor = typer.prompt("Novo Autor", default=livro_original[2])
        preco = obter_preco_valido(str(livro_original[3]))
        data = typer.prompt("Nova Data (YYYY-MM-DD)", default=livro_original[4])
        descricao = typer.prompt("Nova Descrição", default=livro_original[5] or "")
        dados = {
            "titulo": titulo,
            "autor": autor,
            "preco": preco,
            "data_publicacao": data,
            "descricao": descricao
        }
        service.editar_livro(id, dados)
        logger.info(f"Livro editado (ID: {id}): {titulo} por {autor}")
        console.print("[green]✅ Livro atualizado![/green]")
    except Exception as e:
        logger.error(f"Erro ao editar livro: {e}")
        console.print(f"[red]Erro:[/red] {e}")

def menu():
    while True:
        console.print("\n[bold blue]=== MENU BOOKKEEPER ===[/bold blue]")
        console.print("1. Listar Livros")
        console.print("2. Adicionar Livro")
        console.print("3. Buscar Livro por Título")
        console.print("4. Editar Livro")
        console.print("5. Deletar Livro")
        console.print("0. Sair")

        escolha = input("Escolha uma opção: ")
        logger.info(f"Opção escolhida pelo usuário: {escolha}")

        if escolha == "1":
            listar()
        elif escolha == "2":
            adicionar()
        elif escolha == "3":
            buscar_por_titulo()
        elif escolha == "4":
            editar()
        elif escolha == "5":
            deletar()
        elif escolha == "0":
            console.print("[bold green]Até logo![/bold green]")
            logger.info("Aplicação encerrada pelo usuário")
            break
        else:
            console.print("[red]Opção inválida, tente novamente.[/red]")
            logger.warning(f"Opção inválida digitada: {escolha}")

if __name__ == "__main__":
    inicializar_banco()
    logger.info("Aplicação iniciada")
    menu()
