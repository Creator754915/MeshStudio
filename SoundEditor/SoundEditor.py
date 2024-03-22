from ursina import *


class SoundEditor(Entity):
    def __init__(self):
        super(SoundEditor, self).__init__()


if __name__ == "__main__":
    app = Ursina()

    SoundEditor()

    app.run()
