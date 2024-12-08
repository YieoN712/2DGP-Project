from pico2d import *

import game_world

def set_index_fire(index):
    global bg_index
    bg_index = (index == 1)

def is_index_1():
    return bg_index

class Fire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, p_x = 0):
        if Fire.image == None:
            Fire.image = load_image('image/fire.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.total_frame = 12
        self.p = p_x

    def draw(self):
        if self.velocity > 0:
            self.image.clip_draw(int(self.frame) * 102, 0, 102, 54, self.x, self.y - 10, 50, 50)
        else:
            self.image.clip_composite_draw(int(self.frame) * 102, 0, 102, 54, 0, 'h', self.x, self.y - 10, 50, 50)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        frame_speed = 0.1
        self.frame = (self.frame + frame_speed) % self.total_frame

        if self.p - self.x > 250 or self.x - self.p > 250:
            game_world.remove_object(self)
        elif self.x < 0 or self.x > 1440 - 20:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 20,self.x + 10,self.y

    def handle_collision(self, group, other):
        if is_index_1():
            if group == 'rabbit:fire' or group == 'sheep:fire':
                print("fire")
                game_world.remove_object(self)