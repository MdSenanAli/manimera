"""
Manimera Monitor Module.

This module provides the `Monitor` class, which handles execution timing,
signal handling (SIGINT), and process cleanup for the Manimera runtime.
"""

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
    """
    Monitors the execution of the Manimera process.

    This class tracks the execution time, handles keyboard interrupts (SIGINT),
    and ensures that child processes are properly terminated upon exit.
    It also displays a summary panel with the execution status and duration.
    """

    def __init__(self, *, console: Console | None = None, precision: int = 2):
        """
        Initialize the Monitor instance.

        Sets up the start time, signal handlers, and exit hooks.

        Args:
            console (Console | None, optional): A `rich.console.Console` instance.
                If None, a new instance is created. Defaults to None.
            precision (int, optional): The number of decimal places for the
                execution duration display. Defaults to 2.
        """
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
        """
        Handle the SIGINT signal (KeyboardInterrupt).

        Sets the interrupted flag to True and raises KeyboardInterrupt.
        """
        self._interrupted = True
        raise KeyboardInterrupt

    def _terminate_children(self):
        """
        Terminate all child processes spawned by this process.

        On Windows, it uses `taskkill` to kill the process tree.
        On POSIX systems, it kills the entire process group.
        """
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
        """
        Handle the exit of the process.

        Calculates the total execution time, displays a status panel (success or interrupted),
        and ensures child processes are terminated.
        """

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
