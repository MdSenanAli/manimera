# ============================================================
# IMPORTS
# ============================================================

from manim import Scene

from .manager import ACTIVE_SCENE_MANAGER

# ============================================================
# STUDIO RENDER CLASS
# ============================================================


class ManimeraRender:
    """
    Simple wrapper to render a Manim Scene class.
    """

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, scene: Scene = None):
        """
        If a Scene class is provided, instantiate and render it.
        """
        if scene is None:
            scene = ACTIVE_SCENE_MANAGER.get()

        if scene is None:
            print("No Active Scenes Detected.")
            exit()

        video = scene()
        video.render()
