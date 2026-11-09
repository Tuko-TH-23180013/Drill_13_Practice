import game_framework
import game_world
import title_mode
from boy import Boy
from grass import Grass
from pico2d import *
from sdl2 import SDL_KEYDOWN, SDL_KEYUP, SDLK_ESCAPE, SDLK_p


boy = None
paused = False
pause_image = None


def init():
    global boy, paused, pause_image
    game_world.clear()
    paused = False
    pause_image = load_image('pause_overlay.png')
    boy = Boy()
    game_world.add_oject(boy)
    game_world.add_oject(Grass(), 0)


def finish():
    global boy, paused, pause_image
    game_world.clear()
    boy = None
    paused = False
    pause_image = None


def handle_events():
    global paused
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            paused = not paused
        elif paused:
            # Keep key state in sync while paused, without accepting new actions.
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
        else:
            boy.handle_event(event)


def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if paused:
        pause_image.draw(400, 300)
    update_canvas()
