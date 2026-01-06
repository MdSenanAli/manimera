from manimera import *

SETTINGS.set_quality(Quality.STANDARD)


class DemoWire(ManimeraScene):
    def create(self):
        gates = [AND, NAND, OR, XOR, NOR, XNOR, BUFFER, NOT]

        for gate in gates:
            gate_inst = gate()
            if not isinstance(gate_inst, (BUFFER, NOT)):
                i1 = VOID()
                i2 = VOID()
                o1 = VOID()

                i1_grp = VGroup(i1, i2).arrange(DOWN, buff=2).shift(LEFT * 3)
                o1.shift(RIGHT * 3)

                w1 = WIRE(src=i1, dst=gate_inst)
                w2 = WIRE(src=i2, dst=gate_inst)
                w3 = WIRE(src=gate_inst, dst=o1)

                self.play(Write(gate_inst), Write(w1), Write(w2), Write(w3))

                self.wait(1)
                self.play(i1.toggle())
                self.play(i1.toggle(), i2.toggle())
                self.play(i1.toggle())
                self.play(i1.toggle(), i2.toggle())

                self.play(FadeOut(gate_inst, w1, w2, w3))
            else:
                i1 = VOID()
                o1 = VOID()
                i1.shift(LEFT * 3)
                o1.shift(RIGHT * 3)

                w1 = WIRE(src=i1, dst=gate_inst)
                w3 = WIRE(src=gate_inst, dst=o1)

                self.play(Write(gate_inst), Write(w1), Write(w3))

                self.wait(1)
                self.play(i1.toggle())
                self.play(i1.toggle())

                self.play(FadeOut(gate_inst, w1, w3))


if __name__ == "__main__":
    ManimeraRender()
