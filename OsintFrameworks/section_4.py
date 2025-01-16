from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Info Sniper", "description": "Locate an IP"},
    {"name": "iplogger: https://iplogger.com", "description": "Generates a fake link to obtain your victim's IP"},
    {"name": "Nmap: https://nmap.org/download.html#windows", "description": "Nmap is a network scanning and security tool."},
    {"name": "ipvoid: https://www.ipvoid.com", "description": "IP blacklist check, whois lookup, dns lookup, ping, and more!"},
    {"name": "criminalip: https://www.criminalip.io", "description": "Search for information on Domanins, IoTs, Servers and more"}
]

def show_tools():
    table = Table(title="ip Osint")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
