from manimera import *

SETTINGS.set_quality(Quality.MINIMAL)


class LogicGatesExample(ManimeraScene):
    def create(self):
        and_gate = AND()
        nand_gate = NAND()
        buffer_gate = BUFFER()
        not_gate = NOT()
        or_gate = OR()
        nor_gate = NOR()
        xor_gate = XOR()
        xnor_gate = XNOR()
        grp = VGroup(and_gate, nand_gate, buffer_gate, not_gate, or_gate, nor_gate, xor_gate, xnor_gate)
        grp.arrange_in_grid(2, 4, buff=1)
        self.add(grp)


if __name__ == "__main__":
    ManimeraRender()
