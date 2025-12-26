from manimera import *


class DemoAdvanceClockTime(ManimeraScene):
    def create(self):
        clock = Clock()
        self.add(clock)
        self.play(AdvanceClockTime(clock, (3, 30), run_time=5))
        self.wait()


if __name__ == "__main__":
    ManimeraRender()
