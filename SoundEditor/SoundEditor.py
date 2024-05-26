import random

from ursina import *
from ursina.prefabs.file_browser import FileBrowser
from Assets.plugins.Triangle import Triangle
import pygame

app = Ursina()
window.borderless = False
window.cog_menu.enabled = False
window.exit_button.enabled = False
window.fps_counter.enabled = False

sound_list = []
pygame.mixer.init()
playing = False


def add_sound():
    fb = FileBrowser(file_types=('.mp3', '.ogg', '.waw'), enabled=True, z=-1)

    def on_submit(paths):
        for p in paths:
            print('Path: ', p)
            sound_list.append(p)

            Draggable(parent=camera.ui, text=f"Sound {len(sound_list)}",
                      lock=(0, 0, 0),
                      step=(0.05, 0.05, 0.1),
                      scale=(0.35, 0.10),
                      min_x=-0.842, max_x=0.842,
                      min_y=-.4499, max_y=-0.15,
                      radius=0.0,
                      z=0,
                      color=color.random_color())

            print_on_screen(text='Sound import !', scale=1.8, duration=1.4)

    fb.on_submit = on_submit


def start_sound():
    global playing
    for p in sound_list:
        playing = True
        pygame.mixer.music.load(p)
        print(pygame.mixer.music.get_pos())
        pygame.mixer.music.play()
        playing = False


timeline = Entity(parent=camera.ui, model=Quad(radius=0), rotation=(0, 0, 0),
                  position=(0, -0.3, 1),
                  scale=(window.size.x / 700, 0.40),
                  color=color.black66)

timeControl = Draggable(parent=camera.ui,
                        lock=(0, 1, 0),
                        step=(0.01, 0.01, 0.01),
                        scale=(0.01, 0.40),
                        min_x=-.96, max_x=0.96,
                        y=-.3,
                        z=-.1,
                        radius=.0,
                        color=color.white)

runSound = Button(model='circle', position=window.right - 0.03, scale=.05,
                  icon='../icons/run.png',
                  color=color.black50,
                  on_click=start_sound)

timeCode = Entity()

settings = Entity(parent=camera.ui, model=Quad(radius=0), rotation=(0, 0, 0),
                  position=(0, 0.3, 1),
                  scale=(window.size.x / 700, 0.40),
                  color=color.black66)

Text(text="Sound Editor Settings", size=Text.size * 1.2, position=(window.top_left + (.005, -.01)))

Text(text="Name => Good For You", font=('Arial', 20), position=(window.top_left + (.01, -.06)))
Text(text="Time => 3:46", font=('Arial', 20), position=(window.top_left + (.01, -.09)))
Text(text="Path => C:/my/good/music.mp3", font=('Arial', 20), position=(window.top_left + (.01, -.12)))

addSound = Button(text="Import Sound", position=window.right, scale=(.24, 0.05),
                  color=color.black90,
                  on_click=add_sound)

sound = Draggable(parent=camera.ui, text="My Audio 1",
                  lock=(0, 0, 0),
                  step=(0.05, 0.05, 1.2),
                  scale=(0.25, 0.10),
                  min_x=-0.842, max_x=0.842,
                  min_y=-.4499, max_y=-0.15,
                  radius=0.0,
                  color=color.red)

timeControl.x = -.96
sound.position = (.0, -.15)

print(window.size.x / 864, window.aspect_ratio)

print(sound_list)


def input(key):
    if held_keys['shift'] and key == "q":
        add_sound()


def update():
    if playing is True:
        timeControl.x += 0.01


app.run()
