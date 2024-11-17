from pico2d import *

import game_world


class Fire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image('image/fire.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.total_frame = 12

    def draw(self):
        self.image.clip_draw(int(self.frame) * 102, 0, 102, 54, self.x, self.y - 10, 50, 50)
        # draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        frame_speed = 0.1
        self.frame = (self.frame + frame_speed) % self.total_frame

        if self.x < 50 or self.x > 1440 - 50:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 20,self.x + 10,self.y,