from rich.table import Table
from rich.console import Console

console = Console()

# Lista de herramientas específicas de esta sección
tools = [
    {"name": "WhatsMyName Web: https://whatsmyname.app/", "description": "Check where your name appears on the internet"},
    {"name": "Namech_K Web: https://namechk.com/", "description": "Check which domains a name appears in"},
    {"name": "Namecheckr: https://www.namecheckr.com/", "description": "Search for a user ID and see which pages they are registered on."},
    {"name": "namesdir: https://namesdir.com ", "description": "Search by name"},
    {"name": "instantusername: https://instantusername.com", "description": "Search for a user and see which pages or networks they are taken on"}
]

def show_tools():
    table = Table(title="Username Osint")  # Título de la sección
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    # Añadir cada herramienta a la tabla
    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)  # Imprimir la tabla en consola
    input("\nPress Enter to return to the main menu...")  # Esperar al usuario
