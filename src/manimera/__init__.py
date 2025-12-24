# Entry Point To Manimera
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)

# External Libraries
from manim import *
from dotenv import load_dotenv

# Local Imports
from .terminal import Banner, Monitor

# Version
__version__ = "0.1.7"

# Set Environment
load_dotenv()

if __name__ != "__main__":
    Banner(
        library_name="Manimera",
        library_version=__version__,
        subtext="Mathematical visualization made simple by Senan",
    )
    Monitor()
