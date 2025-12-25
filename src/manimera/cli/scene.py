"""
CLI Scene Management Module.

This module handles the creation of new scene files within a chapter,
generating boilerplate code based on `ManimeraScene`.
"""

# ============================================================
# IMPORTS
# ============================================================

import re
from pathlib import Path
from .utils import get_project_root, is_inside_chapter, print_success, print_error, print_info
from .templates import DEFAULT_SCENE_TEMPLATE

# ============================================================
# COMMAND HANDLERS
# ============================================================

def add_scene(name: str):
    """
    Add a new scene to the current chapter.
    
    This command must be run from inside a chapter directory.

    Args:
        name (str): The name of the scene class (CamelCase).
                    The filename will be converted to snake_case.
    """
    current_dir = Path.cwd()

    # Check if we are inside a chapter directly
    if not is_inside_chapter(current_dir):
        # Fallback: check if we are in project root? User requirement: "always be in a chapter"
        # We will enforce being inside the chapter directory for ambiguity reasons.
        print_error("You must be inside a chapter directory to add a scene.")

    try:
        # Validate Project Root linkage
        _ = get_project_root(current_dir)

        # Convert ClassName to snake_case_filename
        class_name = name
        # Regex to convert CamelCase to snake_case
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        snake_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        
        filename = f"{snake_name}.py"
        file_path = current_dir / filename

        if file_path.exists():
            print_error(f"Scene file '{filename}' already exists.")

        # Generate Content
        content = DEFAULT_SCENE_TEMPLATE.format(class_name=class_name)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print_success(f"Created scene [bold cyan]{class_name}[/] in [yellow]{filename}[/]")

    except FileNotFoundError:
        print_error("Not inside a Manimera project.")
    except Exception as e:
        print_error(f"Failed to add scene: {e}")
