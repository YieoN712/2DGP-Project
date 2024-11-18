from pico2d import *
import background
import game_framework
import game_world
import player as Player
import background as BackGround
import title_mode
from fire import set_index_fire
from item import *
from monster import *
from player import set_index_player


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
    global player, heart

    heart = Heart()
    player = Player.Player(heart)
    game_world.add_object(player, 1)
    game_world.add_object(heart, 1)

    grasses = [Grass() for _ in range(5)]
    game_world.add_objects(grasses, 1)

    sheeps = [Sheep() for _ in range(5)]
    game_world.add_objects(sheeps, 1)

    rabbits = [Rabbit() for _ in range(8)]
    game_world.add_objects(rabbits, 1)

    bg = BackGround.BackGround(player)
    game_world.add_object(bg, 0)

    for rabbit in rabbits:
        game_world.add_collision_pair('rabbit:fire', rabbit, None)

    for sheep in sheeps:
        game_world.add_collision_pair('sheep:player',sheep, player)
        game_world.add_collision_pair('sheep:fire', sheep, None)

    for grass in grasses:
        game_world.add_collision_pair('grass:player', grass, player)

def finish():
    game_world.clear()


def update():
    bg = game_world.world[0][0]
    set_visibility(bg.current_index)
    set_index_fire(bg.current_index)
    set_index_player(bg.current_index)

    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume(): pass