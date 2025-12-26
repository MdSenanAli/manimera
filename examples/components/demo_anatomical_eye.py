from manimera import *


class DemoAnatomicalEye(ManimeraScene):
    def create(self):
        eye = AnatomicalEye()
        self.add(eye)


if __name__ == "__main__":
    ManimeraRender()
