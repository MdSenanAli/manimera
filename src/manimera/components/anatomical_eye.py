# ============================================================
# IMPORTS
# ============================================================

from manim import *
from typing import Optional, Tuple

# ============================================================
# CLOCK CLASS
# ============================================================


class AnatomicalEye(VGroup):
    """
    A reusable anatomical eye construct for Manim scenes.

    This class builds an anatomical eye consisting of:
    - An outer circular frame
    - A pupil
    - A iris
    - A central pin
    """

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(
        self,
        radius: float = 1.0,
        **kwargs,
    ):
        self._build_eye()

    # ========================================================
    # PRIVATE METHODS
    # ========================================================

    def _build_eye(self): ...
