from manimera import *


class DemoFeather(ManimeraScene):
    def create(self):
        feather = Feather(curvature=1, barbs=200, max_barb_length=0.5).rotate(PI / 3)
        self.add(feather)


if __name__ == "__main__":
    ManimeraRender()
