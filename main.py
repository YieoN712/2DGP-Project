from pico2d import *
import game_framework
import logo_mode as start_mode
import play_mode

open_canvas(1440, 482)
game_framework.run(start_mode)
close_canvas()