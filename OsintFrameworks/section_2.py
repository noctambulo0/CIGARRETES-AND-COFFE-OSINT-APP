from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Hunter: https://hunter.io", "description": "Check which pages an email is registered on"},
    {"name": "Voilanorbert: voilanorbert.com", "description": "can find anyone's email address"},
    {"name": "Osint.Industries: https://www.osint.industries", "description": "Investigate any email"},
    {"name": "Skymem: https://www.skymem.info", "description": "Find email addresses of companies and people"},
]

def show_tools():
    table = Table(title=" Email Osint")  # Section title
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
