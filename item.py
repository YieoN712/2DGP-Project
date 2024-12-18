from random import random, randint

from pico2d import *

import game_world
import play_mode


def set_index_grass(index):
    global index_g
    index_g = (index == 1)

def is_index_grass_1():
    return index_g

class Heart:
    def __init__(self):
        self.x, self.y = 40, 440
        self.heart = 3
        self.max_health = 3
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
        self.font = load_font('ENCR10B.TTF', 17)

    def draw(self):
        if is_index_grass_1():
                self.image.draw(self.x, self.y, 490 // 10, 706 // 10)

    def update(self):
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def handle_collision(self, group, other):
        if is_index_grass_1() and group == 'player:grass':
            if self in game_world.world[1]:
                game_world.remove_object(self)

class Item:
    def __init__(self):
        self.x, self.y = 400, 150
        self.image = {
            load_image('image/food1.png'),
            load_image('image/food2.png')
        }

    def draw(self):
        self.image[0].draw(self.x, self.y)

    def update(self):
        pass