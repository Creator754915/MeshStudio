from ursina import *


class SoundEditor(Entity):
    def __init__(self, color=color.black10, z=999, **kwargs):
        super().__init__(model=Quad(radius=.0), color=color, z=z, **kwargs)
        self.parent = camera.ui
        self.wdw = window.size.x
        self.wdh = window.size.y
        self.qoef = 100
        self.scale = (self.wdw, 25/self.qoef)
        self.rotation = self.rotation = (0, 90, 0)

        if 'color' in kwargs:
            setattr(self, 'color', kwargs['color'])

        self.timeline = Entity(parent=camera.ui, model='plane', rotation=(0, 0, 90), y=window.bottom,
                               scale=(1, 0.25),
                               color=Color(0, 0, 0, 1))


if __name__ == "__main__":
    app = Ursina()
    window.borderless = False
    window.cog_menu.enabled = False
    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    test = SoundEditor()

    EditorCamera()

    app.run()
