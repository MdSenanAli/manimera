"""
Manimera CLI Entry Point.

This module parses command-line arguments and dispatches control to the
appropriate command handlers in the `cli` package.
"""

# ============================================================
# IMPORTS
# ============================================================

import sys
import argparse
from rich.console import Console

# Import Controllers
from .project import init_project, list_structure
from .chapter import add_chapter
from .scene import add_scene
from .workflow import clean_project, finalize_video

# Import Monitor to disable it for CLI
from ..terminal.monitor import MONITOR

# ============================================================
# MAIN EXECUTION
# ============================================================


def main():
    """Run the Manimera CLI."""
    # Disable monitor output for CLI commands
    MONITOR.disable()

    parser = argparse.ArgumentParser(
        prog="manimera",
        description="Manimera Command Line Interface",
        epilog="Mathematical visualization made simple by Senan.",
    )

    # ========================================================
    # PROJECT COMMANDS
    # ========================================================

    # Check for 'init' as a positional command for standard feel
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Init
    init_parser = subparsers.add_parser(
        "init", help="Initialize a new Manimera project"
    )
    init_parser.add_argument("name", help="Name of the project directory")

    # List
    subparsers.add_parser("list", help="List project structure")

    # Clean
    subparsers.add_parser("clean", help="Clean export and cache directories")

    # Finalize
    subparsers.add_parser("finalize", help="Move latest video/image to final folder")
    # Alias 'mv' for finalize
    subparsers.add_parser("mv", help="Alias for finalize")

    # ========================================================
    # FLAGS (As requested: --add-chapter, etc.)
    # ========================================================

    parser.add_argument(
        "--add-chapter", metavar="NAME", help="Add a new chapter to the project"
    )
    parser.add_argument(
        "--add-scene", metavar="NAME", help="Add a new scene to the current chapter"
    )

    # Parse
    args = parser.parse_args()

    # Dispatch
    if args.command == "init":
        init_project(args.name)
    elif args.command == "list":
        list_structure()
    elif args.command == "clean":
        clean_project()
    elif args.command in ["finalize", "mv"]:
        finalize_video()

    # Handle Flags (Prioritized if command is missing)
    elif args.add_chapter:
        add_chapter(args.add_chapter)
    elif args.add_scene:
        add_scene(args.add_scene)

    else:
        # If no arguments, print help
        parser.print_help()


if __name__ == "__main__":
    main()
