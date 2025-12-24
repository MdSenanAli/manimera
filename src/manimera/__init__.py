# Entry Point To Manimera

# External Libraries
from manim import *
from dotenv import load_dotenv

# Local Imports
from .terminal import print_banner

# Version
__version__ = "0.1.7"

# Set Environment
load_dotenv()

if __name__ != "__main__":
    print_banner("Manimera", __version__, "Easy animations by Senan")
