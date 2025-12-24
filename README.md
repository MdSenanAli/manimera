# Manimera

**Manimera** is a Python library designed to simplify the creation of **Manim animations**. It provides an easy-to-use interface for animating mathematical concepts, graphics, and educational content—perfect for YouTube creators and educators.  

This library is developed by **Senan**, creator of educational videos using Manim.

---

## Features

- Simplifies Manim animation creation with minimal code
- Integrates easily with existing Manim projects
- Suitable for educational videos, tutorials, and visual explanations
- Supports quick rendering and exporting of animations

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

class SceneName(ManimeraScene):
    def create(self):
        # Your Animation Logic Here

if __name__ == "__main__":
    ManimeraRender(SceneName)
```


---

## License

This project is licensed under the **MIT License**.

---

## About

Created by **Senan**, Manimera helps streamline animation production for teaching and learning, making it easier to create engaging educational content.
