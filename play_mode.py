import game_framework
import game_world
import title_mode
from boy import Boy
from grass import Grass
from pico2d import *
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE, SDLK_i, SDLK_p


boy = None
paused = False
pause_image = None
item_image = None
item_selecting = False


def init():
    global boy, paused, pause_image, item_image, item_selecting
    game_world.clear()
    paused = False
    pause_image = load_image('pause_overlay.png')
    item_image = load_image('item_select.png')
    item_selecting = False
    boy = Boy()
    game_world.add_oject(boy)
    game_world.add_oject(Grass(), 0)


def finish():
    global boy, paused, pause_image, item_image, item_selecting
    game_world.clear()
    boy = None
    paused = False
    pause_image = None
    item_image = None
    item_selecting = False


def handle_events():
    global paused, item_selecting
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if not item_selecting:
                paused = not paused
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if not paused:
                item_selecting = not item_selecting
        elif item_selecting:
            # Keep held movement keys in sync without accepting actions.
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
        elif paused:
            # Keep key state in sync while paused, without accepting new actions.
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
        else:
            boy.handle_event(event)


def update():
    if not paused and not item_selecting:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if paused:
        pause_image.draw(400, 300)
    if item_selecting:
        item_image.draw(400, 300)
    update_canvas()
