from manimera import *


class DemoCathedralLamp(ManimeraScene):
    def create(self):
        lamp = CathedralLamp()
        lamp.set_intensity(0.5)
        self.add(lamp)


if __name__ == "__main__":
    ManimeraRender()
