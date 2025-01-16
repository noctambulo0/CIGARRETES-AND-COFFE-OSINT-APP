from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Sherlock: https://github.com/sherlock-project/sherlock", "description": "Find usernames across social networks."},
    {"name": "Wfuzz: https://github.com/xmendez/wfuzz", "description": "Web application fuzzing tool for testing."},
    {"name": "Dnsmap: https://github.com/makefu/dnsmap", "description": "DNS network mapping and enumeration tool."},
    {"name": "Mat2: https://github.com/Mat2/Mat2", "description": "Metadata removal tool for files"},
    {"name": "Cain & Abel: https://www.oxid.it/cain.html", "description": "assword recovery and network sniffing tool."},
    {"name": "Social-Engineer Toolkit (SET): https://github.com/trustedsec/social-engineer-toolkit", "description": "Phishing attack and social engineering tool."},

]

def show_tools():
    table = Table(title="HACKING APPS")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
