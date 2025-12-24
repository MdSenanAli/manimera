from manimera import *

SETTINGS.set_quality(Quality.MINIMAL)

class ClockExample(ManimeraScene):
    def create(self):
        clock = Clock()
        self.add(clock)

if __name__ == "__main__":
    ManimeraRender()
