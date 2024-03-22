import json

from ursina import *
from Animation.timeline_creator import KeyframesManager


class Timeline(Entity):
    def __init__(self, min=0, max=100, default=None, height=Text.size, text='', dynamic=False,
                 bar_color=color.black66, list_to_anim=list, **kwargs):
        super().__init__(add_to_scene_entities=False)  # add later, when __init__ is done
        if list_to_anim is None:
            list_to_anim = []
        self.parent = camera.ui
        self.vertical = False
        self.min = min
        self.max = max
        self.list_to_anim = list_to_anim

        if default is None:
            default = min
        self.default = default
        self.step = 0
        self.height = height

        self.on_value_changed = None  # set this to a function you want to be called when the slider changes
        self.setattr = None  # set this to (object, 'attrname') to set that value when the slider changes

        self.label = Text(parent=self, origin=(0.5, 0), x=-0.025, text=text)

        self.bg = Entity(parent=self, model=Quad(scale=(.525, height), radius=0, segments=3),
                         origin_x=-0.25, collider='box', color=bar_color)

        self.knob = Draggable(parent=self, min_x=0, max_x=.5, min_y=0, max_y=.5, step=self.step,
                              model=Quad(radius=0, scale=(0.01, height)), collider='box', color=color.light_gray,
                              text='0', text_origin=(0, -.55), z=-.1)

        self.add_key_button = Button(parent=self, scale=(0.125 / 1.2, 0.125 / 1.2), text="Add", x=0.625,
                                     radius=0, on_click=self.add_keyframe)

        self.kf = Button(scale=(0.01, 0.01), rotation=(0, 0, 45), radius=0, color=color.white, disabled=True,
                         visible=False)

        print(self.height, self.scale_x)

        def bg_click():
            self.knob.x = mouse.point[0]
            self.knob.start_dragging()

        self.bg.on_click = bg_click

        def drop():
            self.knob.z = -.1
            if self.setattr:
                if isinstance(self.setattr[0], dict):  # set value of dict
                    self.setattr[0][self.setattr[1]] = self.value
                else:  # set value of Entity
                    setattr(self.setattr[0], self.setattr[1], self.value)

            if self.on_value_changed:
                self.on_value_changed()

        self.knob.drop = drop
        self._prev_value = self.default
        self.value = self.default
        self.dynamic = dynamic  # if set to True, will call on_value_changed() while dragging. if set to False, will only call on_value_changed() after dragging.

        self.knob.text_entity.text = str(round(self.default, 2))

        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.vertical:
            self.rotation_z = -90
            self.knob.lock = (1, 0, 0)
            self.knob.text_entity.rotation_z = 90
            self.knob.text_entity.position = (.015, 0)
        else:
            self.knob.lock = (0, 1, 1)
            self.knob.text_entity.y = height / 2

        scene.entities.append(self)

    @property
    def value(self):
        val = lerp(self.min, self.max, self.knob.x * 2)
        if isinstance(self.step, int) and not self.step == 0:
            val = int(round(val, 0))

        return val

    @value.setter
    def value(self, value):
        self.knob.x = (value - self.min) / (self.max - self.min) / 2
        self.slide()

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
        self.knob.step = value / (self.max - self.min) / 2

    def update(self):
        if self.knob.dragging:
            self.slide()

        if held_keys['right arrow'] and self.value < 100:
            self.value += 1

        if held_keys['left arrow'] and self.value > 0:
            self.value -= 1

    def slide(self):
        t = self.knob.x / .5

        if self.step > 0:
            if isinstance(self.step, int) or self.step.is_integer():
                self.knob.text_entity.text = str(self.value)

        if self.dynamic and self._prev_value != t:
            if self.on_value_changed:
                self.on_value_changed()

            if self.setattr:
                target_object, attr = self.setattr
                setattr(target_object, attr, self.value)

            self._prev_value = t

        invoke(self._update_text, delay=1 / 60)

    def _update_text(self):
        self.knob.text_entity.text = str(round(self.value, 2))

    def __setattr__(self, name, value):
        if name == 'eternal':
            try:
                self.label.eternal = value
                self.bg.eternal = value
                self.knob.eternal = value
            except:
                pass
        try:
            super().__setattr__(name, value)
        except Exception as e:
            return e

    def add_keyframe(self):
        for cube in self.list_to_anim:
            print(cube.name)

        print(self.value)
        duplicate(self.kf, visible=True, x=self.knob.x)


if __name__ == '__main__':
    app = Ursina()

    cube_nmb = []

    slider = Timeline(height=Text.size * 5, step=1, list_to_anim=cube_nmb)

    cube1 = Draggable(parent=scene, model="cube", color=color.white, name="HELLO", collider="box",
                      postion=(0, 0, 0), scale=(1, 1, 1))

    cube_nmb.append(cube1)

    EditorCamera()

    app.run()
