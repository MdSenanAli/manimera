from manimera import *


class DemoPendulum(ManimeraScene):
    def create(self):
        pendulum = Pendulum(string_length=5, bob_radius=0.5, bob_color=BLUE)
        self.add(pendulum)


if __name__ == "__main__":
    ManimeraRender()
