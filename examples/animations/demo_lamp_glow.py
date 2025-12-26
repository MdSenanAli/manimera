from manimera import *


class DemoLampGlow(ManimeraScene):
    def create(self):
        lamp = CathedralLamp()
        self.add(lamp)
        self.play(LampGlow(lamp, max_light_opacity=0.2))


if __name__ == "__main__":
    ManimeraRender()
