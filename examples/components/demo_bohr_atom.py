from manimera import *


class DemoBohrAtom(ManimeraScene):
    def create(self):
        atom = BohrAtom(AtomType.Hydrogen)
        self.add(atom)


if __name__ == "__main__":
    ManimeraRender()
