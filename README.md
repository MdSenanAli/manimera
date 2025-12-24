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

## Quick Start

Here’s a basic example of creating a simple animation:

```python
from manimera import *

SETTINGS.set_quality(Quality.PREMIUM)


class CircleCreation(ManimeraScene):
    def create(self):
        circle = Circle(1)
        self.play(Create(circle))


if __name__ == "__main__":
    # This will auto-detect the latest `ManimeraScene` class and render it.
    ManimeraRender()

```


---

## License

This project is licensed under the **MIT License**.

---

## About

Created by **Senan**, Manimera helps streamline animation production for teaching and learning, making it easier to create engaging educational content.
