from random import random

from pico2d import  *
import game_framework
import game_world
from state_machine import *
import time
import random


PIXEL_PER_METER = (13.0 / 0.5)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

def set_visibility_c(index):
    global _visible_C
    _visible_C = (index != 1)

def is_visible_c():
    return _visible_C

class Customer:

    def __init__(self):
        self.x, self.y = -80, 80
        self.line_x = 0
        self.frame = 0
        self.image = load_image('image/customer.png')

        self.food = random.randint(1, 2)
        self.received_food = False

    def handle_event(self, event):
        pass

    def update(self):
        if not self.received_food:
            if self.x <= self.line_x:
                self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
                self.x += RUN_SPEED_PPS * game_framework.frame_time
        else:
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
            self.x -= RUN_SPEED_PPS * game_framework.frame_time
            if self.x < - 100:
                game_world.remove_object(self)

    def draw(self):
        if is_visible_c():
            font = load_font('ENCR10B.TTF', 17)
            if not self.received_food:
                font.draw(self.x - 30, self.y + 70, f'food: {self.food:d}', (55, 0, 0))
                self.image.clip_draw(int(self.frame % 4) * (284 // 4), 0, 284 // 4, 228 // 2, self.x, self.y, 90, 90)
            else:
                self.image.clip_composite_draw(int(self.frame % 4) * (284 // 4), 0, 284 // 4, 228 // 2, 0, 'h', self.x,
                                               self.y, 90, 90)
    def get_bb(self):
        return self.x - 40, self.y - 35, self.x + 40, self.y + 40

    def handle_collision(self, group, other):
        pass

