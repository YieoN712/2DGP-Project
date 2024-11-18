from random import random, randint

from pico2d import load_image


def set_index_grass(index):
    global index_g
    index_g = (index == 1)

def is_index_1():
    return index_g

class Heart:
    def __init__(self):
        self.x, self.y = 40, 440
        self.heart = 3
        self.image = load_image('image/heart.png')

    def draw(self):
        for i in range(self.heart):
            self.image.draw(self.x + i * 60, self.y, 382 // 6, 653 // 6)

    def update(self):
        pass

    def decrease_heart(self):
        if self.heart > 0:
            self.heart -= 1


class Grass:
    def __init__(self):
        self.x, self.y = randint(200, 1400), 75
        self.count = 5
        self.image = load_image('image/grass.png')

    def draw(self):
        if is_index_1():
                self.image.draw(self.x, self.y, 490 // 2, 706 // 2)

    def update(self):
        pass