# Manimera

**Manimera** is a wrapper around **Manim Community** designed to simplify the creation of mathematical visualizations, with a focus on **production pipelines** and ease of use. It provides an intuitive interface for animating mathematical concepts, graphics, and educational content—perfect for YouTube creators and educators.

This library is developed by **Senan**, creator of educational videos using Manim.

---

## Features

- **Simplified Workflow**: Create Manim animations with minimal boilerplate code.
- **Production Ready**: Designed for efficient rendering pipelines and project management.
- **Fully Documented**: Comprehensive docstrings and type hints for a better development experience.
- **Easy Integration**: Seamlessly integrates with existing Manim projects.
- **Quick Rendering**: optimized settings for fast rendering and exporting.

---

## Installation

You can install Manimera using `pip`:

```bash
pip install manimera
````

Or, if you are using `uv`:

```bash
uv pip install manimera
```

After installation, add Manimera to your project:

```bash
uv add manimera
```

---

## Manimera CLI

Manimera comes with a dedicated Command Line Interface (CLI) to help you manage your animation projects efficiently.

### 1. Initialize a Project
Create a new project structure with default chapters and utility scripts:
```bash
manimera init MyProject
```
This creates a hierarchy:
- `Chapter-000` / `001` / `002`
  - `assets/`: For your local media files.
  - `export/`: Where your rendered videos and images go.
- `scripts/`: Production utility scripts (like cleaning).

### 2. Manage Chapters & Scenes
Add new chapters or scenes with boilerplate code automatically generated:
```bash
# Add a new chapter
manimera --add-chapter Introduction

# Add a scene (must be run inside a chapter folder)
manimera --add-scene MyFirstScene
```

### 3. Workflow Utilities
Clean your project or finalize your renders:
```bash
# Remove cache and clean assets
manimera clean

# Copy the latest render to the 'final' directory with context-aware renaming
manimera finalize # or use 'manimera mv'
```

### 4. List Project Structure
See an overview of your project's chapters and scenes:
```bash
manimera list
```

---

## Quick Start

Here’s a basic example of creating a simple animation:

```python
# ClockCreation.py
from manimera import *

# ClockCreation class
class ClockCreation(ManimeraScene):
    def create(self):
        clock = Clock()
        self.play(Create(clock))

# Entry point
if __name__ == "__main__":
    # This will auto-detect the `ClockCreation` class and render it.
    ManimeraRender() 
```

---

## License

This project is licensed under the **MIT License**.

---

## About

Created by **Senan**, Manimera helps streamline animation production for teaching and learning, making it easier to create engaging educational content.
