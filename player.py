import time

from pico2d import  *
import background as bg
import game_framework
import game_world
from fire import Fire
from state_machine import StateMachine, time_out, space_down, right_down, left_up, left_down, right_up, start_event

PIXEL_PER_METER = (10.0 / 0.5)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 7

def set_index_player(index):
    global bg_index
    bg_index = (index == 1)

def is_index_p_1():
    return bg_index


class Idle:
    @staticmethod
    def enter(p, e):
        if start_event(e):
            p.action = 3
            p.face_dir = -1
        elif right_down(e) or left_up(e):
            p.action = 3
            p.face_dir = -1
        elif left_down(e) or right_up(e):
            p.action = 2
            p.face_dir = 1

        p.frame = 0
        p.wait_time = get_time()

    @staticmethod
    def exit(p, e):
        if space_down(e):
            p.fire()

    @staticmethod
    def do(p):
        p.frame = (p.frame + 4 * ACTION_PER_TIME * game_framework.frame_time) % 4
        if get_time() - p.wait_time > 8:
            p.state_machine.add_event(('TIME_OUT', 0))

    @staticmethod
    def draw(p):
        p.image.clip_draw(int(p.frame) * 50, p.action * 100, 50, 100, p.x, p.y)


class Sleep:
    @staticmethod
    def enter(p, e):
        if start_event(e):
            p.face_dir = -1
            p.action = 2
        p.frame = 0

    @staticmethod
    def exit(p, e):
        pass

    @staticmethod
    def do(p):
        pass

    @staticmethod
    def draw(p):
        if p.face_dir == 1:
            p.image.clip_composite_draw(0, 200, 50, 100,
                                        3.141592 / 2, '', p.x - 30, p.y - 30, 50, 100)
        else:
            p.image.clip_composite_draw(50, 300, 50, 100,
                                        -(3.141592 / 2), '', p.x + 30, p.y - 30, 50, 100)


class Run:
    @staticmethod
    def enter(p, e):
        if right_down(e) or left_up(e):     # right
            p.dir, p.face_dir, p.action = 1, 1, 0
        elif left_down(e) or right_up(e):   # left
            p.dir, p.face_dir, p.action = -1, -1, 1

    @staticmethod
    def exit(p, e):
        if space_down(e):
            p.fire()

    @staticmethod
    def do(p):
        p.frame = (p.frame + FRAME_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % 7
        p.x += p.dir * RUN_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(p):
        p.image.clip_draw(int(p.frame) * 50, p.action * 100, 50, 100, p.x, p.y)



class Player:

    def __init__(self, h):
        self.x, self.y = 950, 75
        self.face_dir = -1
        self.font = load_font('ENCR10B.TTF', 16)
        self.max_mana = 5
        self.mana = self.max_mana
        self.image = load_image('image/player.png')

        self.state_machine = StateMachine(self)
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle},
                Run: {right_down: Idle, left_down: Idle, left_up: Idle, right_up: Idle, space_down: Run},
                Sleep: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle}
            }
        )

        self.recharge_timer = None
        self.recharge_delay = 2.0

        self.collision_time = 0
        self.cooldown_collision = 2.0

        self.heart = h

        self.colliding_with_grass = None

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def update(self):
        self.state_machine.update()

        self.x = max(0, min(self.x, 1420))

        if self.mana <= 0 and self.recharge_timer is None:
            self.recharge_timer = get_time()  # 충전 시작 시간 설정
        elif self.recharge_timer is not None:
            if get_time() - self.recharge_timer >= self.recharge_delay:
                self.mana = self.max_mana  # 공 충전
                self.recharge_timer = None


    def fire(self):
        if self.mana > 0:
            self.mana -= 1
            fire = Fire(self.x, self.y, self.face_dir * 5, self.x)
            game_world.add_object(fire, 1)
            game_world.add_collision_pair('rabbit:fire', None, fire)
            game_world.add_collision_pair('sheep:fire', None, fire)


    def draw(self):
        self.state_machine.draw()

        if self.recharge_timer is None:
            self.font.draw(self.x - 25, self.y + 50, f'mana:{self.mana:d}', (255, 255, 0))
        elif self.recharge_timer is not None:
            self.font.draw(self.x - 35, self.y + 50, f'RECHARGE', (0, 0, 255))
        # if self.state_machine.cur_state == Idle:
        #     draw_rectangle(*self.get_bb())
        # elif self.state_machine.cur_state == Sleep:
        #     draw_rectangle(*self.get_bb())
        # elif self.state_machine.cur_state == Run:
        #     draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.state_machine.cur_state == Idle:
            return self.x - 20, self.y - 50, self.x + 15, self.y + 40
        elif self.state_machine.cur_state == Sleep and self.face_dir == 1:
            return self.x - 70, self.y - 45, self.x + 20, self.y - 15
        elif self.state_machine.cur_state == Sleep and self.face_dir == -1:
            return self.x - 20, self.y - 45, self.x + 70, self.y - 15
        elif self.state_machine.cur_state == Run:
            return self.x - 20, self.y - 50, self.x + 15, self.y + 40

    def handle_collision(self, group, other):
        if is_index_p_1():
            if group == 'player:grass':
                self.colliding_with_grass = other
            if group == 'sheep:player':
                current_time = time.time()
                if current_time - self.collision_time >= self.cooldown_collision:
                    self.heart.decrease_heart()
                    self.collision_time = current_time
