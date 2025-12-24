from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style


class Banner:
    def __init__(self, library_name: str, library_version: str, subtext: str = ""):
        self.library_name = library_name
        self.library_version = library_version
        self.subtext = subtext
        self.console = Console()

        self._show()

    def _show(self):
        title = Text()
        title.append(
            f"{self.library_name}", style=Style(color="bright_magenta", bold=True)
        )
        title.append(
            f" v{self.library_version}", style=Style(color="bright_yellow", bold=True)
        )

        subtitle = Text(
            f"✨  {self.subtext}  ✨",
            style=Style(color="bright_cyan", italic=True, bold=True),
            justify="center",
        )

        panel = Panel(
            subtitle,
            title=title,
            border_style="bright_magenta",
            padding=(1, 4),
        )
        self.console.print(panel)
