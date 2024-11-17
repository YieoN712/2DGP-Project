import random
from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 4

class Rabbit:
    def __init__(self):
        self.x, self.y = random.randint(400, 1420), 75
        self.image = load_image('image/rabbit.png')
        self.frame = 0
        self.dir = random.choice([-1, 1])
        self.size = 100

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1400:
            self.dir = -1
        elif self.x < 400:
            self.dir = 1
        self.x = clamp(400, self.x, 1400)


    def draw(self):
        if self.dir < 0:
            self.image.clip_composite_draw(int(self.frame) * (504 // 4), 0, 126, 180, 0, 'h', self.x, self.y, self.size, self.size)
        else:
            self.image.clip_draw(int(self.frame) * (504 // 4), 0, 126, 180,self.x, self.y, self.size, self.size)


class Sheep:
    def __init__(self):
        self.x, self.y = random.randint(1420 - 950, 1420), 75
        self.image = load_image('image/sheep.png')
        self.frame = 0
        self.dir = random.choice([-1, 1])
        self.size = 100

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1400:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1400)


    def draw(self):
        if self.dir > 0:
            self.image.clip_composite_draw(int(self.frame) * (320 // 4), 0, (320 // 4), 80, 0, 'h', self.x, self.y, self.size, self.size)
        else:
            self.image.clip_draw(int(self.frame) * (320 // 4), 0, (320 // 4), 80,self.x, self.y, self.size, self.size)