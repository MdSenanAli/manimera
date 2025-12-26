from manimera import *


class DemoBrick(ManimeraScene):
    def create(self):
        brick = Brick()
        self.add(brick)


if __name__ == "__main__":
    ManimeraRender()
