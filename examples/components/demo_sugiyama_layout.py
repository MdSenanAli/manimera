from manimera import *


class DemoSugiyamaLayout(ManimeraScene):
    def create(self):
        layout = SugiyamaLayout(
            [
                ("i1", VOID, []),
                ("i2", VOID, []),
                ("a1", AND, ["i1", "i2"]),
                ("o1", VOID, ["or"]),
                ("x1", XOR, ["i1", "i2"]),
                ("or", OR, ["i1", "x1"]),
            ]
        )

        self.add(layout.get_layout(x_spacing=1.4, y_spacing=1.5))


if __name__ == "__main__":
    ManimeraRender()
