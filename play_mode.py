import clear_mode
import game_state
import player as Player
import background as BackGround
import title_mode
from customer import set_visibility_c, Customer
from fire import set_index_fire
from item import *
from monster import *
from player import set_index_player


def reset_game():
    global player, heart
    finish()  # 현재 게임 상태 초기화
    init()  # 새 게임 상태 설정

    # 다음 날로 넘어가기
    game_state.current_day += 1

    # 체력 회복 및 벌금 계산
    lost_health = heart.max_health - heart.heart
    if lost_health > 0:
        player.money -= lost_health * 50





    heart.heart = heart.max_health  # 체력 회복

    bg.reset_background()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            reset_game()
        else:
            for obj in game_world.world[0]:
                obj.handle_event(event)
            player.handle_event(event)


def init():
    global player, heart, bg

    heart = Heart()
    player = Player(heart)
    game_world.add_object(player, 2)
    game_world.add_object(heart, 1)

    num_customers = random.randint(3, 8)  # 3~8명의 손님 랜덤 생성
    customers = [Customer() for _ in range(num_customers)]
    game_state.customer_count = len(customers)

    # 손님 줄 서기 (각 손님의 x 좌표를 일정 간격으로 설정)
    start_x = -80
    spacing = 100  # 손님 간 간격
    for i, customer in enumerate(customers):
        customer.x = start_x - (spacing * i)
        customer.line_x = 550 - (80 * i)
        game_world.add_object(customer, 1)

    num_grass = random.randint(5, 8)
    grasses = [Grass() for _ in range(num_grass)]
    game_world.add_objects(grasses, 1)

    sheeps = [Sheep(player) for _ in range(4)]
    game_world.add_objects(sheeps, 2)

    rabbits = [Rabbit(player) for _ in range(7)]
    game_world.add_objects(rabbits, 2)

    bg = BackGround.BackGround(player)
    game_world.add_object(bg, 0)

    # collision
    for rabbit in rabbits:
        game_world.add_collision_pair('rabbit:fire', rabbit, None)

    for sheep in sheeps:
        game_world.add_collision_pair('sheep:player',sheep, player)
        game_world.add_collision_pair('sheep:fire', sheep, None)

    for grass in grasses:
        game_world.add_collision_pair('player:grass', player, grass)

def finish():
    game_world.clear()
    game_world


def update():
    bg = game_world.world[0][0]

    set_visibility(bg.current_index)
    set_visibility_c(bg.current_index)
    set_index_fire(bg.current_index)
    set_index_player(bg.current_index)
    set_index_grass(bg.current_index)

    game_world.update()
    game_world.handle_collisions()

    if player.money >= 1000:  # 예: 1,000원이 넘으면 클리어
        game_framework.change_mode(clear_mode)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause(): pass
def resume(): pass