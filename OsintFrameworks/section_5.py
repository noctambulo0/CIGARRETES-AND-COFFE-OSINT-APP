from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "We are working on this", "description": "SON"},
        {"name": "CIGARRETE AND COFFE BY NOCTAMBULO", "description": "I love you"},

]

def show_tools():
    table = Table(title="COMING SON")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
