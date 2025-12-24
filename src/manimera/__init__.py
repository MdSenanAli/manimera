"""
Manimera Library.

Manimera is a wrapper around Manim Community that provides a simplified
interface for creating mathematical visualizations, with a focus on
production pipelines and ease of use.
"""

# Entry Point To Manimera
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)

# External Libraries
from manim import *

# Local Imports
from .terminal import *
from .runtime import *
from .theme import *
from .components import *
from .animations import *

# Version
__version__ = "0.1.13"

# Print Banner And Monitor Execution
if __name__ != "__main__":
    Banner(
        library_name="Manimera",
        library_version=__version__,
        subtext="Mathematical visualization made simple by Senan",
    )
    Monitor()
