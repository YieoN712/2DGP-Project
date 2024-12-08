from pico2d import *

import game_world
from customer import trigger_customer
from item import Item


class BackGround:
    def __init__(self, player):
        self.image = [
            load_image('image/background_main.jpg'),
            load_image('image/background_hunt.jpg')
        ]
        self.panel = load_image('image/panel.png')
        self.current_index = 0
        self.show_message = False
        self.p = player

        self.panel_visible = False  # 패널 상태 변수
        self.selected_food = None  # 선택된 음식 변수


    def draw(self):
        self.image[self.current_index].draw(1440 // 2, 482 // 2)
        font = load_font('ENCR10B.TTF', 20)
        if self.show_message and self.p.x >= 1440 - 70:
            font.draw(1340, 150, 'press f', (255, 255, 0))
        elif self.show_message and self.p.x <= 70:
            font.draw(30, 150, 'press f', (255, 255, 0))
        elif self.show_message and self.p.x <= 1000 and self.p.x >= 900:
            font.draw(910, 210, 'press s', (0, 0, 190))
        elif self.show_message and self.p.x <= 700 and self.p.x >= 650:
            font.draw(635, 150, 'press c', (230, 0, 255))
        elif self.show_message and self.p.x >= 400 and self.p.y <= 500:
            font.draw(440, 160, 'press e', (50, 50, 225))

        if self.panel_visible:  # 패널
            self.panel.draw(720, 340)
            panel_font = load_font('ENCR10B.TTF', 18)
            panel_font.draw(750, 290, "2: Grass 1", (255, 255, 255))
            panel_font.draw(750, 275, "   Meat 2", (255, 255, 255))
            panel_font.draw(580, 290, "1: Meat 2", (255, 255, 255))
            panel_font.draw(600, 420, f'steak: {self.p.food1:d}', (0, 0, 0))
            panel_font.draw(760, 420, f'burger: {self.p.food2:d}', (0, 0, 0))

    def update(self):
        if self.p.x >= 1440 - 70 and self.current_index == 0:
            self.show_message = True
        elif self.p.x <= 70 and self.current_index == 1:
            self.show_message = True
        elif self.p.x >= 900 and self.p.x <= 1000:
            if self.current_index == 0:
                self.show_message = True
        elif self.p.x >= 650 and self.p.x <= 700:
            if self.current_index == 0:
                self.show_message = True
        elif self.p.x >= 300 and self.p.x <= 600:
            if self.current_index == 0:
                self.show_message = True
        else:
            self.show_message = False

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_f and self.show_message:
                self.current_index = (self.current_index + 1) % len(self.image)
                if self.p.x <= 40:
                    self.p.x = 1440 - 30
                else:
                    self.p.x = 30

            if event.key == SDLK_c and self.show_message:
                self.panel_visible = not self.panel_visible  # 패널 토글

            if self.panel_visible:  # 패널이 활성화된 동안
                if event.key == SDLK_2:  # 1번 키로 음식 제작
                    if self.p.grass_count >= 1 and self.p.meat_count >= 2:
                        self.p.grass_count -= 1
                        self.p.meat_count -= 2
                        self.p.food1 += 1
                elif event.key == SDLK_1:  # 2번 키로 음식 제작
                    if self.p.meat_count >= 2:
                        self.p.meat_count -= 2
                        self.p.food2 += 1
