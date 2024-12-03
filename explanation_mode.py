from pico2d import *
from sdl2 import *

import game_framework
import play_mode


def init():
    global image
    image = load_image('image/lobby.jpg')

def finish():
    global image
    del image

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            game_framework.change_mode(play_mode)


def draw():
    clear_canvas()
    image.draw(1440 // 2, 482 // 2)
    update_canvas()

def pause(): pass
def resume(): pass