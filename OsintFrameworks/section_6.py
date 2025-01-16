from rich.table import Table
from rich.console import Console

console = Console()

tools = [
    {"name": "Inflact Instagram Viewer (Anonymous): https://inflact.com/instagram-viewer/profile/?profile=", "description": "Anon Instagram profile viewer, no trace."},
    {"name": "Osintgram: https://github.com/Datalux/Osintgram", "description": "Osintgram is an OSINT tool on Instagram to collect, analyze, and run reconnaissance."},
    {"name": "urlebird: https://urlebird.com//", "description": "Check tik tok profiles being anonymous"},
    {"name": "Telegago: https://cse.google.com/cse?&cx=006368593537057042503:efxu7xprihg", "description": "Search for channels or telegram or related words"},
    {"name": "redditmetis: https://redditmetis.com/#", "description": "Get Reddit user statistics"}
]

def show_tools():
    table = Table(title="Social Networks osint")
    table.add_column("Tool", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="red")

    for tool in tools:
        table.add_row(tool['name'], tool['description'])

    console.print(table)
    input("\nPress Enter to return to the main menu...")
