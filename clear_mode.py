from pico2d import *
import game_framework
import game_state
import title_mode

def init():
    global image
    image = load_image('image/clear_screen.jpg')  # 클리어 화면 이미지

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)  # 타이틀 화면으로 돌아가기
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_mode(title_mode)  # ENTER로도 타이틀로 돌아가기

def update():
    pass

def draw():
    clear_canvas()
    image.draw(1440 // 2, 482 // 2)
    font = load_font('ENCR10B.TTF', 50)
    font.draw(600, 400, 'Clear!!',(255,255,255))
    font = load_font('ENCR10B.TTF', 50)
    font.draw(500, 350, '-------------',(255,255,255))
    font = load_font('ENCR10B.TTF', 30)
    font.draw(600, 300, f'Day: {game_state.current_day:d}',(255,255,255))
    font = load_font('ENCR10B.TTF', 30)
    font.draw(600, 250, f'total: {game_state.all_money:d}won',(255,255,255))
    font = load_font('ENCR10B.TTF', 20)
    font.draw(550, 100, 'press ESC or Enter to title', (255, 255, 255))
    update_canvas()

def pause(): pass
def resume(): pass
