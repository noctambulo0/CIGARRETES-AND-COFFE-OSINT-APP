from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Whocalld: https://whocalld.com", "description": "Telephone number information."},
    {"name": "truecaller: https://www.truecaller.com", "description": "The World Best Caller ID and Spam Blocking App"},
    {"name": "spydialer: https://www.spydialer.com", "description": " Collected Billions of Phone Numbers and Created one Seriously Free Reverse Phone Number"},
    {"name": "phonevalidator: https://www.phonevalidator.com", "description": "VALIDATE PHONE NUMBERS ABOVE FOR FREE TO IDENTIFY PHONE LINE TYPE AND PHONE COMPANY"},
    {"name": "fonefinder: https://www.fonefinder.net", "description": "Search international telephone numbers"}
]

def show_tools():
    table = Table(title="Phone number OSINT")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
