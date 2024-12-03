import random
from pico2d import *

import background
import game_framework
import game_world
import player

PIXEL_PER_METER = (10.0 / 0.5)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 4

# _visible = False

def set_visibility(index):
    global _visible
    _visible = (index == 1)

def is_visible():
    return _visible

class Rabbit:
    def __init__(self):
        self.x, self.y = random.randint(400, 1420), 75
        self.image = load_image('image/rabbit.png')
        self.frame = 0
        self.dir = random.choice([-1, 1])
        self.size = 100
        self.p = player

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1400:
            self.dir = -1
        elif self.x < 400:
            self.dir = 1
        self.x = clamp(400, self.x, 1400)


    def draw(self):
        if is_visible():
            if self.dir < 0:
                self.image.clip_composite_draw(int(self.frame) * (504 // 4), 0, 126, 180, 0, 'h', self.x, self.y, self.size, self.size)
            else:
                self.image.clip_draw(int(self.frame) * (504 // 4), 0, 126, 180,self.x, self.y, self.size, self.size)

            draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def get_bb(self):
        if int(self.frame) == 0 or int(self.frame) == 3:
            return self.x - 35, self.y - 45, self.x + 40, self.y
        elif int(self.frame) == 1:
            return self.x - 35, self.y - 15, self.x + 40, self.y + 45
        else:
            return self.x - 40, self.y - 12, self.x + 40, self.y + 38

    def handle_collision(self, group, other):
        if is_visible():
            if group == 'rabbit:fire':
                print("Rabbit hit by fire")
                game_world.remove_object(self)


class Sheep:
    def __init__(self):
        self.x, self.y = random.randint(1420 - 950, 1420), 75
        self.image = load_image('image/sheep.png')
        self.frame = 0
        self.speed = 2  # 클수록 느림
        self.dir = random.choice([-1, 1])
        self.size = 100
        self.alpha = 1.0

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAME_PER_ACTION
        self.x += (RUN_SPEED_PPS * self.dir * game_framework.frame_time) / self.speed
        if self.x > 1400:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1400)


    def draw(self):
        if is_visible():
            self.image.opacify(self.alpha)
            if self.dir > 0:
                self.image.clip_composite_draw(int(self.frame) * (320 // 4), 0, (320 // 4), 80, 0, 'h', self.x, self.y, self.size, self.size)
            else:
                self.image.clip_draw(int(self.frame) * (320 // 4), 0, (320 // 4), 80,self.x, self.y, self.size, self.size)

            draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def get_bb(self):
        return  self.x - 40, self.y - 35, self.x + 40, self.y + 40

    def handle_collision(self, group, other):
        if is_visible():
            if group == 'sheep:fire' and self.alpha == 1.0:
                print("sheep hit by fire")
                self.alpha = 0.5
                self.speed = 0.3
            elif group == 'sheep:fire' and self.alpha == 0.5:
                print("sheep hit by fire")
                game_world.remove_object(self)