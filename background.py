from pico2d import *


class BackGround:
    def __init__(self, player):
        self.image = [
            load_image('image/background_main.jpg'),
            load_image('image/background_hunt.jpg')
        ]
        self.current_index = 1
        self.show_message = False
        self.p = player

    def draw(self):
        self.image[self.current_index].draw(1440 // 2, 482 // 2)
        if self.show_message and self.p.x >= 1440 - 70:
            font = load_font('ENCR10B.TTF', 16)
            font.draw(1340, 150, 'press f', (255, 255, 0))
        elif self.show_message and self.p.x <= 70:
            font = load_font('ENCR10B.TTF', 16)
            font.draw(30, 150, 'press f', (255, 255, 0))

    def update(self):
        if self.p.x >= 1440 - 70 and self.current_index == 0:
            self.show_message = True
        elif self.p.x <= 70 and self.current_index == 1:
            self.show_message = True
        else:
            self.show_message = False

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_f and self.show_message:
            self.current_index = (self.current_index + 1) % len(self.image)
            if self.p.x <= 40:
                self.p.x = 1440 - 30
            else:
                self.p.x = 30