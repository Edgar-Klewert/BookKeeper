import typer
from rich.console import Console
from rich.table import Table
from database.init_db import inicializar_banco
import service.livro_service as service
from utils.logger import logger

app = typer.Typer()
console = Console()

def listar():
    logger.info("Listando livros")
    livros = service.listar_livros()
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
        autor = typer.prompt("Autor")
        preco = float(typer.prompt("Preço"))
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
        id = int(typer.prompt("ID do livro para deletar"))
        service.remover_livro(id)
        logger.info(f"Livro deletado (ID: {id})")
        console.print("[green]✅ Livro deletado.[/green]")
    except Exception as e:
        logger.error(f"Erro ao deletar livro (ID: {id}): {e}")
        console.print(f"[red]Erro:[/red] {e}")

def buscar():
    try:
        id = int(typer.prompt("ID do livro para buscar"))
        livro = service.buscar_livro(id)
        if not livro:
            console.print("[red]Livro não encontrado.[/red]")
            logger.warning(f"Tentativa de buscar livro inexistente (ID: {id})")
            return
        logger.info(f"Livro encontrado (ID: {id})")
        console.print(f"[cyan]ID:[/cyan] {livro[0]}")
        console.print(f"[cyan]Título:[/cyan] {livro[1]}")
        console.print(f"[cyan]Autor:[/cyan] {livro[2]}")
        console.print(f"[cyan]Preço:[/cyan] R${livro[3]:.2f}")
        console.print(f"[cyan]Data:[/cyan] {livro[4]}")
        console.print(f"[cyan]Descrição:[/cyan] {livro[5] or '-'}")
    except Exception as e:
        logger.error(f"Erro ao buscar livro (ID: {id}): {e}")
        console.print(f"[red]Erro:[/red] {e}")

def editar():
    try:
        id = int(typer.prompt("ID do livro para editar"))
        livro_original = service.buscar_livro(id)
        if not livro_original:
            console.print("[red]Livro não encontrado.[/red]")
            logger.warning(f"Tentativa de editar livro inexistente (ID: {id})")
            return
        titulo = typer.prompt("Novo Título", default=livro_original[1])
        autor = typer.prompt("Novo Autor", default=livro_original[2])
        preco = typer.prompt("Novo Preço", default=str(livro_original[3]))
        data = typer.prompt("Nova Data (YYYY-MM-DD)", default=livro_original[4])
        descricao = typer.prompt("Nova Descrição", default=livro_original[5] or "")
        dados = {
            "titulo": titulo,
            "autor": autor,
            "preco": float(preco),
            "data_publicacao": data,
            "descricao": descricao
        }
        service.editar_livro(id, dados)
        logger.info(f"Livro editado (ID: {id}): {titulo} por {autor}")
        console.print("[green]✅ Livro atualizado![/green]")
    except Exception as e:
        logger.error(f"Erro ao editar livro (ID: {id}): {e}")
        console.print(f"[red]Erro:[/red] {e}")

def menu():
    while True:
        console.print("\n[bold blue]=== MENU BOOKKEEPER ===[/bold blue]")
        console.print("1. Listar Livros")
        console.print("2. Adicionar Livro")
        console.print("3. Buscar Livro por ID")
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
            buscar()
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
