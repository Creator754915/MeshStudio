from ursina import *


class DirectionBox(Entity):
    def __init__(self, parent=camera.ui, model="../Assets/Models/WorldDirection.obj", camera=None, scale=.02, z=-30, **kwargs):
        super().__init__(parent=parent, model=model, camera=camera, scale=scale, z=z, **kwargs)
        # self.position = Vec2(.8, 0.4)
        self.position = window.top_right - Vec2(.065, .1)

    def input(self, key):
        if held_keys['shift']:
            if key == '1':
                self.camera.animate_rotation((0, 0, 0))  # front
            elif key == '2':
                self.camera.animate_rotation((0, 180, 0))  # front
            elif key == '3':
                self.camera.animate_rotation((0, -90, 0))  # left
            elif key == '4':
                self.camera.animate_rotation((0, 90, 0))  # right
            elif key == '5':
                self.camera.animate_rotation((90, 0, 0))  # top
            elif key == '6':
                self.camera.animate_rotation((-90, 0, 0))  # bottom

    def update(self):
        self.rotation = -self.camera.rotation
1


if __name__ == "__main__":
    app = Ursina()
    window.fullscreen = False
    window.borderless = False
    window.exit_button.enabled = False
    window.fps_counter.enabled = False

    ce = EditorCamera()

    DirectionBox(camera=ce)

    app.run()
