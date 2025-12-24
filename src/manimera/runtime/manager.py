from typing import Type, Optional


class ActiveSceneManager:
    """
    Singleton manager for tracking the currently active scene.
    """

    _instance: Optional["ActiveSceneManager"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._active_scene = None
        return cls._instance

    def set(self, scene_cls: Type) -> None:
        """Set the active scene class."""
        self._active_scene = scene_cls

    def get(self) -> Optional[Type]:
        """Return the currently active scene class."""
        return self._active_scene

    def clear(self) -> None:
        """Clear the active scene."""
        self._active_scene = None


# Singleton instance
ACTIVE_SCENE_MANAGER = ActiveSceneManager()
