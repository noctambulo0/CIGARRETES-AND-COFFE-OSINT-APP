from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Shodan: https://www.shodan.io", "description": "search engine for internet connected devices"},
    {"name": "Nikto: https://nikto.online", "description": "Analyze domains and web pages"},
    {"name": "Urlscan: https://urlscan.io/search/#*", "description": "Search for domains, IPs, filenames, hashes, ASNs"},
    {"name": "dailychanges: https://www.dailychanges.com", "description": "monitors DNS changes for domain names"},
    {"name": "synapsint: https://synapsint.com/index.php", "description": "Unified OSINT Investigation Tool"}
]

def show_tools():
    table = Table(title="Domain Osint")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
