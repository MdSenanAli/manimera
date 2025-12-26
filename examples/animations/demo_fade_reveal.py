from manimera import *


class DemoFadeReveal(ManimeraScene):
    def create(self):
        self.play(FadeReveal(Square()))


if __name__ == "__main__":
    ManimeraRender()
