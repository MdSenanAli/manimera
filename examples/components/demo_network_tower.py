from manimera import *

SETTINGS.set_quality(Quality.MINIMAL)

class NetworkTowerExample(ManimeraScene):
    def create(self):
        tower = NetworkTower()
        self.add(tower)

if __name__ == "__main__":
    ManimeraRender()
