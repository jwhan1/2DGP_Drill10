from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Labs\Lecture15_Time\grass.png')
        self.ruler_image = load_image('Labs/Lecture15_Time/ruler.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        self.ruler_image.draw(800, 350)


