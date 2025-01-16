import os
from rich.console import Console
from rich.panel import Panel
from OsintFrameworks import section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8, section_9 # Importar todas las secciones

console = Console()

def clear_screen():
    # Limpiar la pantalla
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def show_header():
    ascii_art = """
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
    """
    header_content = (
        f"{ascii_art}\n"
        "[bold cyan]CIGARRETE AND COFFE OSINT[/bold cyan]\n"
        "[bold white]Created by: NOCTAMBULO[/bold white]\n"
        "[bold magenta]GitHub: https://github.com/noctambulo0[/bold magenta]\n"
        "[bold green]Twitter: @Nocta.[/bold green]\n"
        "[bold red]Version: 1.0.[/bold red]"
    )
    clear_screen()
    console.print(Panel(header_content, title="OSINT Framework", expand=False))

def main_menu():
    clear_screen()
    show_header()
    console.print("[bold green]1.[/bold green] Search Username")
    console.print("[bold green]2.[/bold green] Search Email")
    console.print("[bold green]3.[/bold green] Search domain name")
    console.print("[bold green]4.[/bold green] Search IP address")
    console.print("[bold green]5.[/bold green] Search images/videos/docs")
    console.print("[bold green]6.[/bold green] Social networks")
    console.print("[bold green]7.[/bold green] Search phone number")
    console.print("[bold green]8.[/bold green] Geolocation tools")
    console.print("[bold green]9.[/bold green] Hacking tools ")
    console.print("[bold red]0.[/bold red] Exit")
    console.print("[bold purple]❤️ THX FOR USING CIGARRETE AND COFFE OSINT[/bold purple]")

    choice = input("\nChoose a section: ")

    if choice == '1':
        section_1.show_tools()
    elif choice == '2':
        section_2.show_tools()
    elif choice == '3':
        section_3.show_tools()
    elif choice == '4':
        section_4.show_tools()
    elif choice == '5':
        section_5.show_tools()
    elif choice == '6':
        section_6.show_tools()
    elif choice == '7':
        section_7.show_tools()
    elif choice == '8':
        section_8.show_tools()
    elif choice == '9':
        section_9.show_tools()
    elif choice == '0':
        console.print("Exiting... Bye!")
        exit()
    else:
        console.print("[bold red]Invalid choice! Please try again.[/bold red]")
        main_menu()

if __name__ == "__main__":
    main_menu()
