from ursina import *
from ObjectOriented.main import launch
from Assets.plugins.Background import Background

launcher = Ursina()
launcher.title = "MeshStudio Launcher"
window.borderless = False
window.fullscreen = False
window.exit_button.enabled = False
window.fps_counter.enabled = False


def run():
    application.quit()
    launch()


Sky(texture='sky_sunset')

title = Text(parent=camera.ui, text="MeshStudio", size=Text.size * 5)

runBtn = Button(parent=camera.ui, text="Start New Project", scale=(0.25, 0.1), radius=0.1,
                y=0)

settingsBtn = Button(parent=camera.ui, text="Setting", scale=(0.25, 0.1), radius=0.1,
                     y=-.15)

exitBtn = Button(parent=camera.ui, text="Exit", color=color.red.tint(-.3), scale=(0.25, 0.1), radius=0.1,
                 y=-.3)

launcher.run()
