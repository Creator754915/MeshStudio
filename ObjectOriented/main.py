from ObjectOriented.SceneEditor import SceneEditor
from ursina import *


def launch():
    app = Ursina()
    window.borderless = False
    window.fullscreen = False
    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    SceneEditor()

    app.run()


if __name__ == "__main__":
    launch()
