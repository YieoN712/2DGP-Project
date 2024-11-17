from pico2d import *

import background
import game_framework
import game_world
import player as Player
import background as BackGround
import title_mode
from monster import *


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            for obj in game_world.world[0]:
                obj.handle_event(event)
            player.handle_event(event)


def init():
    global player

    player = Player.Player()
    game_world.add_object(player, 1)

    sheep = [Sheep() for _ in range(5)]
    game_world.add_objects(sheep, 1)

    rabbit = [Rabbit() for _ in range(8)]
    game_world.add_objects(rabbit, 1)

    bg = BackGround.BackGround(player)
    game_world.add_object(bg, 0)

def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume(): pass