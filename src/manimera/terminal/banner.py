# Imports
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


def print_banner(library_name: str, library_version: str, subtext: str):
    console = Console()

    title = Text(library_name, style="bold blue")
    title.append(f" v{library_version}", style="bold yellow")

    subtitle = Text(subtext, style="dim italic cyan")

    panel = Panel(subtitle, title=title, border_style="bright_blue", padding=(1, 2))

    console.print(panel)
