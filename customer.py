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
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.image = load_image('image/customer.png')

        self.food = random.randint(0, 1)

    def handle_event(self, event):
        pass

    def update(self):
        if self.x <= 550:
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
            self.x += RUN_SPEED_PPS * game_framework.frame_time
        # self.x = clamp(0, self.x, 550)

    def draw(self):
        if is_visible_c():
            self.image.clip_draw(int(self.frame % 4) * (284 // 4), 0, 284 // 4, 228 // 2,self.x, self.y, 90, 90)

    def get_bb(self):
        pass

    def handle_collision(self, group, other):
        pass