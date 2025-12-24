# Entry Point To Manimera
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)

# External Libraries
from manim import *

# Local Imports
from .terminal import Banner, Monitor
from .runtime import Settings, Quality

# Version
__version__ = "0.1.10"

# Global Setting Object
SETTINGS = Settings()

# Print Banner And Monitor Execution
if __name__ != "__main__":
    Banner(
        library_name="Manimera",
        library_version=__version__,
        subtext="Mathematical visualization made simple by Senan",
    )
    Monitor()
