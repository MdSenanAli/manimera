"""
Manimera Render Module.

This module provides the `ManimeraRender` class, which handles the instantiation
and rendering of Manim scenes. It integrates with the `ActiveSceneManager` to
automatically detect the scene to render if none is explicitly provided.
"""

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
    Wrapper class to render a Manim Scene.

    This class simplifies the rendering process by automatically resolving
    the active scene from the `ActiveSceneManager` if not provided.
    """

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def __init__(self, scene: Scene = None):
        """
        Initialize the renderer and execute the render loop.

        If a scene class is provided, it is instantiated and rendered.
        Otherwise, the active scene is retrieved from the `ActiveSceneManager`.

        Args:
            scene (Scene, optional): The scene class to render. Defaults to None.
        """
        if scene is None:
            scene = ACTIVE_SCENE_MANAGER.get()

        if scene is None:
            print("No Active Scenes Detected.")
            exit()

        video = scene()
        video.render()
