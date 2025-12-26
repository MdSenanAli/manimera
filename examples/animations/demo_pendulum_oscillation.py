from manimera import *


class DemoPendulumOscillation(ManimeraScene):
    def create(self):
        pendulum = Pendulum()
        self.add(pendulum)

        self.play(
            PendulumOscillation(
                pendulum, amplitude=30 * DEGREES, frequency=1.0, damping=0.0, phase=0.0
            ),
            run_time=5,
        )


if __name__ == "__main__":
    ManimeraRender()
