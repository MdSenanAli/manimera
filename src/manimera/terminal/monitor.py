import time
import atexit
import signal
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


class Monitor:
    """
    Monitors total runtime and reports exit status.
    """

    def __init__(
        self,
        *,
        enabled: bool = True,
        console: Console | None = None,
        precision: int = 2,
    ):
        if not enabled:
            return

        self._start = time.perf_counter()
        self._interrupted = False
        self._precision = precision
        self._console = console or Console()

        signal.signal(signal.SIGINT, self._handle_sigint)
        atexit.register(self._handle_exit)

    def _handle_sigint(self, *_):
        self._interrupted = True
        raise KeyboardInterrupt

    def _handle_exit(self):
        elapsed = time.perf_counter() - self._start
        duration = f"{elapsed:.{self._precision}f}s"

        if self._interrupted:
            message = Text(
                f"⏹  Execution interrupted · {duration}",
                style="yellow",
                justify="center",
            )
            border = "yellow"
        else:
            message = Text(
                f"✔  Execution completed · {duration}",
                style="green",
                justify="center",
            )
            border = "green"

        panel = Panel(
            message,
            border_style=border,
            padding=(0, 2),
        )

        self._console.print(panel)
