"""
CLI Workflow Module.

This module provides automation for common workflow tasks such as cleaning
export directories and finalizing/renaming rendered videos.
"""

# ============================================================
# IMPORTS
# ============================================================

import os
import shutil
from pathlib import Path
from rich.prompt import Confirm
# We can reuse the clean logic from templates or just implement it direct
from .utils import get_project_root, print_success, print_error, print_info, CONSOLE

# ============================================================
# COMMAND HANDLERS
# ============================================================

def clean_project():
    """
    Remove all 'export' and '__pycache__' directories in the project.
    """
    try:
        root = get_project_root()
        
        dirnames = ["__pycache__", "export"]
        deleted = 0
        
        if not Confirm.ask(f"Are you sure you want to delete all {dirnames} folders in [cyan]{root.name}[/]?"):
            print_info("Operation cancelled.")
            return

        for dirpath in root.rglob("*/"):
            if dirpath.name in dirnames:
                try:
                    shutil.rmtree(dirpath)
                    CONSOLE.print(f"[green] - {dirpath.relative_to(root)}[/]")
                    deleted += 1
                except Exception:
                    CONSOLE.print(f"[red] - {dirpath.relative_to(root)}[/]")

        print_success(f"Deleted {deleted} directories.")

    except FileNotFoundError:
        print_error("Not inside a Manimera project.")


def finalize_video():
    """
    Move the latest rendered video to a 'final' directory.
    
    This command looks for the most recently modified video file in the 
    current directory's 'export' folder (recursive), and moves it to the 
    project's 'final' directory, renaming it with context.
    """
    try:
        root = get_project_root()
        current_dir = Path.cwd()
        
        # We expect to be in a chapter or near where we rendered
        # Logic: Find latest .mp4 under current directory's export/
        
        export_base = current_dir / "export"
        if not export_base.exists():
             print_error("No 'export' directory found in current path.")

        # Find all mp4 files recursively in export/
        mp4_files = list(export_base.rglob("*.mp4"))
        
        if not mp4_files:
            print_error("No rendered videos found in export/.")

        # Sort by modification time (latest first)
        latest_video = max(mp4_files, key=os.path.getmtime)
        
        # Prepare destination: root/final
        final_dir = root / "final"
        final_dir.mkdir(exist_ok=True)
        
        # Construct new filename
        # Format: <chapter_context>-<resolution>-<original_name>.mp4
        # We need to deduce chapter and resolution from path
        # Path is usually: .../Chapter-NNN/export/SceneName/WxH/filename.mp4
        
        # Try to infer chapter name from current dir or video parent
        chapter_name = "Ref"
        rel_path = latest_video.relative_to(root)
        
        # Heuristic: split path
        parts = rel_path.parts
        # parts[0] might be Chapter-NNN
        if len(parts) > 0 and "Chapter" in parts[0]:
            chapter_name = parts[0]
            
        resolution = latest_video.parent.name # Parent is WxH usually
        original_name = latest_video.name
        
        new_name = f"{chapter_name}-{resolution}-{original_name}"
        dest_path = final_dir / new_name

        shutil.copy2(latest_video, dest_path)
        
        print_success(f"Finalized video to: [bold cyan]{dest_path}[/]")

    except FileNotFoundError:
        print_error("Not inside a Manimera project.")
    except Exception as e:
        print_error(f"Failed to finalize video: {e}")
