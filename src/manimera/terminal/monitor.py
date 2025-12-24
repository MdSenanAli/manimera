import os
import signal
import time
import atexit
import platform
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


class Monitor:
    def __init__(self, *, console: Console | None = None, precision: int = 2):
        self._start = time.perf_counter()
        self._interrupted = False
        self._precision = precision
        self._console = console or Console()
        self._is_windows = platform.system() == "Windows"

        if not self._is_windows:
            # POSIX: isolate process group
            os.setpgrp()

        signal.signal(signal.SIGINT, self._handle_sigint)
        atexit.register(self._handle_exit)

    def _handle_sigint(self, *_):
        self._interrupted = True
        raise KeyboardInterrupt

    def _terminate_children(self):
        try:
            if self._is_windows:
                # Windows: kill process tree
                subprocess.run(
                    ["taskkill", "/F", "/T", "/PID", str(os.getpid())],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                # POSIX: kill entire process group
                pgid = os.getpgrp()
                os.killpg(pgid, signal.SIGTERM)
        except Exception:
            pass  # never crash on cleanup

    def _handle_exit(self):

        elapsed = time.perf_counter() - self._start
        duration = f"{elapsed:.{self._precision}f}s"

        text = Text(
            (
                f"⏹  Execution interrupted · {duration}"
                if self._interrupted
                else f"✔  Execution completed · {duration}"
            ),
            style="yellow" if self._interrupted else "green",
            justify="center",
        )

        panel = Panel(
            text,
            border_style="yellow" if self._interrupted else "green",
            padding=(0, 2),
        )

        self._console.print(panel)
        self._terminate_children()
