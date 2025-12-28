from manimera import *


class DemoBohrAtom(ManimeraScene):
    def create(self):
        atom = BohrAtom(AtomType.Oganesson, atom_scale=5)
        name = atom.get_name().next_to(atom, direction=DOWN, buff=0.4)
        self.add(atom, name)


if __name__ == "__main__":
    ManimeraRender()
