from pico2d import *


class BackGround:
    def __init__(self, player):
        self.image = [
            load_image('image/background_main.jpg'),
            load_image('image/background_hunt.jpg')
        ]
        self.current_index = 0
        self.show_message = False
        self.p = player

        self.panel_visible = False  # 패널 상태 변수
        self.selected_food = None  # 선택된 음식 변수

    def draw(self):
        self.image[self.current_index].draw(1440 // 2, 482 // 2)
        if self.show_message and self.p.x >= 1440 - 70:
            font = load_font('ENCR10B.TTF', 20)
            font.draw(1340, 150, 'press f', (255, 255, 0))
        elif self.show_message and self.p.x <= 70:
            font = load_font('ENCR10B.TTF', 20)
            font.draw(30, 150, 'press f', (255, 255, 0))
        elif self.show_message and self.p.x <= 1000 and self.p.x >= 900:
            font = load_font('ENCR10B.TTF', 20)
            font.draw(910, 150, 'press e', (230, 0, 255))
        elif self.show_message and self.p.x <= 700 and self.p.x >= 650:
            font = load_font('ENCR10B.TTF', 20)
            font.draw(635, 150, 'press c', (230, 0, 255))

        if self.panel_visible:  # 패널 표시
            panel_font = load_font('ENCR10B.TTF', 25)
            draw_rectangle(540, 240, 900, 440)  # 패널 배경
            panel_font.draw(550, 400, "1: Grass 1 + Meat 2", (0, 255, 0))
            panel_font.draw(550, 360, "2: Meat 2", (255, 0, 0))

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
                if event.key == SDLK_1:  # 1번 키로 음식 제작
                    if self.p.grass_count >= 1 and self.p.meat_count >= 2:
                        self.p.grass_count -= 1
                        self.p.meat_count -= 2
                        print("음식 1 제작 완료!")
                elif event.key == SDLK_2:  # 2번 키로 음식 제작
                    if self.p.meat_count >= 2:
                        self.p.meat_count -= 2
                        print("음식 2 제작 완료!")