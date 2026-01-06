from manimera import *

SETTINGS.set_quality(Quality.STANDARD)


class DemoDFlipFlop(ManimeraScene):
    def create(self):
        d, clk = self._create_d_flip_flop()

        for i in range(20):
            if i % 5 == 0:
                self.play(d.toggle(2), clk.toggle(2))
            else:
                self.play(clk.toggle(2))

    def _create_d_flip_flop(self):
        rect = Rectangle(width=6, height=4.5)
        rect.set_stroke(width=5, color=WHITE)

        D = VOID()
        CLOCK = VOID()

        D.next_to(rect, LEFT, buff=1.5).shift(DOWN * 1)
        CLOCK.next_to(rect, LEFT, buff=1.5).shift(DOWN * 1.75)

        D_label = Text("D").scale(0.5).next_to(D, LEFT)
        CLOCK_label = Text("CLK").scale(0.5).next_to(CLOCK, LEFT)

        D_label.add_updater(lambda m: m.next_to(D, LEFT))
        CLOCK_label.add_updater(lambda m: m.next_to(CLOCK, LEFT))

        not1 = NOT()

        nand11 = NAND()
        nand12 = NAND()

        layer1 = VGroup(nand11, nand12)

        nand21 = NAND()
        nand22 = NAND()

        layer2 = VGroup(nand21, nand22)

        layer1.arrange(DOWN, buff=1).shift(LEFT * 0.5)
        layer2.arrange(DOWN, buff=1).shift(RIGHT)

        not1.next_to(nand11, LEFT, buff=1)

        Q = VOID()
        Q_BAR = VOID()

        Q1 = VOID()
        Q1_BAR = VOID()

        Q1.next_to(nand21, RIGHT, buff=1)
        Q1_BAR.next_to(nand22, RIGHT, buff=1)
        Q.next_to(Q1, RIGHT, buff=1)
        Q_BAR.next_to(Q1_BAR, RIGHT, buff=1)

        Q_label = Text("Q'").scale(0.5).next_to(Q, RIGHT)
        Q_BAR_label = Text("Q").scale(0.5).next_to(Q_BAR, RIGHT)

        Q1_L = VOID()
        Q1_BAR_L = VOID()

        Q1_L.next_to(Q1, DOWN, buff=0.3)
        Q1_BAR_L.next_to(Q1_BAR, UP, buff=0.3)

        Q2_L = VOID()
        Q2_BAR_L = VOID()

        Q2_L.next_to(Q1_L, LEFT, buff=2)
        Q2_BAR_L.next_to(Q1_BAR_L, LEFT, buff=2)

        self.add(
            rect,
            D_label,
            CLOCK_label,
            layer1,
            layer2,
            not1,
            Q,
            Q_BAR,
            Q_label,
            Q_BAR_label,
            Q1,
            Q1_BAR,
            Q1_L,
            Q1_BAR_L,
            Q2_L,
            Q2_BAR_L,
        )

        # WIRES
        w1 = WIRE(D, not1)
        w2 = WIRE(D, nand12)
        w3 = WIRE(not1, nand11)

        w4 = WIRE(CLOCK, nand11, alpha=0.8)
        w5 = WIRE(CLOCK, nand12, alpha=0.8)

        w6 = WIRE(nand11, nand21)
        w7 = WIRE(nand21, Q1)

        w8 = WIRE(Q1, Q)
        w9 = WIRE(Q1_BAR, Q_BAR)
        w10 = WIRE(nand22, Q1_BAR)

        w11 = WIRE(Q1, Q1_L)
        w12 = WIRE(Q1_BAR, Q1_BAR_L)

        w13 = WIRE(Q2_BAR_L, nand22, alpha=0)
        w14 = WIRE(Q2_L, nand21, alpha=0)

        w15 = WIRE(nand12, nand22)

        w16 = WIRE(Q1_L, Q2_BAR_L)
        w17 = WIRE(Q1_BAR_L, Q2_L)

        wires = VGroup(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17)
        for wire in wires:
            wire.update_path()

        self.add(wires)
        return D, CLOCK


if __name__ == "__main__":
    ManimeraRender()
