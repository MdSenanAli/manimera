# ============================================================
# IMPORTS
# ============================================================

import os
import ast
import inspect
import tempfile

from enum import Enum
from manim import config
from typing import Dict
from typing import Final
from datetime import datetime
from dataclasses import dataclass

from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

from ..constants import BACKGROUND_GREY

# ============================================================
# QUALITY
# ============================================================


class Quality(Enum):
    MINIMAL = "minimal"
    STANDARD = "standard"
    PREMIUM = "premium"


# ============================================================
# PROFILE CLASS
# ============================================================


@dataclass(frozen=True)
class RenderProfile:
    width: int
    height: int
    fps: int


# ============================================================
# PROFILES
# ============================================================

PROFILES: Final[Dict[Quality, RenderProfile]] = {
    Quality.MINIMAL: RenderProfile(1280, 720, 15),
    Quality.STANDARD: RenderProfile(1920, 1080, 30),
    Quality.PREMIUM: RenderProfile(3840, 2160, 60),
}

# ============================================================
# SETTINGS CLASS
# ============================================================


class Settings:
    """
    Singleton class to manage Manim render settings
    and log them in a Rich panel.
    """

    # ========================================================
    # SINGLETON IMPLEMENTATION
    # ========================================================

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, profiles: Dict[Quality, RenderProfile] = PROFILES):
        self.console = Console()
        self.profiles = profiles

    # ========================================================
    # PRIVATE HELPERS
    # ========================================================

    def _set_width(self, pixel_width: int = 1920):
        config.pixel_width = pixel_width

    def _set_height(self, pixel_height: int = 1080):
        config.pixel_height = pixel_height

    def _set_frame_rate(self, fps: int = 60):
        config.frame_rate = fps

    def _set_background(self, color: str = BACKGROUND_GREY):
        config.background_color = color

    def _set_caller_file(self, profile: RenderProfile):
        try:
            # Resolve caller file
            frame = inspect.stack()[-1]
            caller_file = frame.filename
        except IndexError as e:
            raise RuntimeError("Unable to inspect call stack") from e

        caller_dir = os.path.dirname(os.path.abspath(caller_file))

        # export/{width}x{height}/
        resolution = f"{profile.width}x{profile.height}"
        export_dir = os.path.join(caller_dir, "export", resolution)
        os.makedirs(export_dir, exist_ok=True)

        # Scene name
        scene_name = self._get_last_scene_instance(caller_file)

        # Timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}-{scene_name}"

        config.output_file = os.path.join(export_dir, filename)

    def _set_caching(self, value=False):
        config.disable_caching = not value

    def _get_last_scene_instance(self, caller_file) -> str:
        with open(caller_file, "r", encoding="utf-8") as f:
            source = f.read()

        tree = ast.parse(source)

        # Search from bottom -> top of the file
        for node in reversed(tree.body):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    # Works for Scene and StudioScene
                    if isinstance(base, ast.Name) and base.id in {
                        "ManimeraScene",
                    }:
                        return node.name

        raise ValueError(f"No Scene Object in file: {caller_file}.")

    def _set_temp_media_dir(self, name: str = "manimera_media"):
        base_temp = tempfile.gettempdir()
        media_dir = os.path.join(base_temp, name)

        os.makedirs(media_dir, exist_ok=True)
        config.media_dir = media_dir

    def _log_panel(self, level: str, profile: RenderProfile):
        """
        Prints the current render settings in a Rich panel.
        """
        table = Table(show_header=False, box=None)
        table.add_row("Profile", level)
        table.add_row("Width", f"{profile.width} px")
        table.add_row("Height", f"{profile.height} px")
        table.add_row("FPS", f"{profile.fps}")
        table.add_row("Background", str(config.background_color))
        table.add_row("Caching", str(not config.disable_caching))
        table.add_row("Save Last Frame", str(config.save_last_frame))
        table.add_row("Frame Width", f"{config.frame_width:.2f} units")
        table.add_row("Frame Height", f"{config.frame_height:.2f} units")
        table.add_row("Media Dir", f"{config.media_dir}")
        table.add_row("Output File", f"{config.output_file}")

        title = Text("Render Settings", style="bold cyan")
        panel = Panel(table, title=title, border_style="cyan", padding=(1, 2))
        self.console.print(panel)

    # ========================================================
    # PUBLIC INTERFACE
    # ========================================================

    def set_quality(self, level: Quality, caching: bool = True):
        """
        Sets render quality according to a preset profile.
        """
        profile = self.profiles[level]

        self._set_caching(caching)
        self._set_width(profile.width)
        self._set_height(profile.height)
        self._set_frame_rate(profile.fps)
        self._set_background(BACKGROUND_GREY)

        # Generate filename using render profile
        self._set_caller_file(profile)

        # Temp media directory with constant name
        self._set_temp_media_dir()

        # Logging Data at End
        self._log_panel(level.name, profile)


SETTINGS = Settings()
