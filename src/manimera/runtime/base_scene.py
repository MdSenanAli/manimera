# ============================================================
# IMPORTS
# ============================================================

from abc import ABC, abstractmethod
from manim import *

from .manager import ACTIVE_SCENE_MANAGER

# ============================================================
# MANIMERA SCENE BASE CLASS
# ============================================================


class ManimeraScene(Scene, ABC):
    # ========================================================
    # PRIVATE HELPERS
    # ========================================================

    def __watermark(self, name="Senan"):
        """
        Returns a small watermark at the bottom-left corner.
        """
        return (
            Tex(name)
            .scale_to_fit_height(0.15)
            .to_corner(DL)
            .set_color(WHITE)
            .shift(DL * 0.3)
        )

    # ========================================================
    # ABSTRACT METHODS
    # ========================================================

    @abstractmethod
    def create(self) -> None:
        """
        Must be implemented by child classes to define scene content.
        """
        ...

    # ========================================================
    # CONSTRUCT
    # ========================================================

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        ACTIVE_SCENE_MANAGER.set(cls)

    # ========================================================
    # CONSTRUCT
    # ========================================================

    def construct(self) -> None:
        """
        Entry point for Manim to render the scene.
        Adds watermark, then calls the child's create() method.
        """
        # Add Watermark
        self.add(self.__watermark("Senan"))

        # Create content from child class
        self.create()
