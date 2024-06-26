import colorama
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from Assets.plugins.CheckBox import CheckBox
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(title='Texture Node Editor', borderless=False, fullscreen=False, development_mode=False, vsync=True)

test = Vec4(0, 0, 0, 0.72)


class ConnectorLine(Entity):
    def __init__(self, start_entity, end_entity, color=color.white):
        super().__init__(
            model='quad',
            color=color,
            scale=(0, 10),
            parent=scene)

        self.start_entity = start_entity
        self.end_entity = end_entity
        self.update_line()

    def update_line(self):
        self.position = (self.start_entity.world_position + self.end_entity.world_position) / 2
        self.look_at(self.end_entity.world_position)


class ModelNode(Draggable):
    def __init__(self, text='Model', position=(0, 0), scale=(.3, .3, .3), color=Color(0, 0, 0, 0.72)):
        super().__init__(
            text=text,
            text_origin=(0, .4),
            position=position,
            scale=scale,
            radius=0.05,
            color=color,
            highlight_color=color,
            texture="white_cube")

        self.texture_attachment = Button(model='circle', position=(-.5, 0, -.01), scale=.07, parent=self)
        self.texture_attachment.on_click = self.update_line

        self.path = InputField(default_value='path', limit_content_to='_./abcdefghijklmnopqrstuvwxyz',
                               character_limit=13, position=(0, .2, -.01), scale=(.9, .15), parent=self)
        self.scaleText = Text(text='Scale', position=(-.43, .04, -.01), scale=3.25, parent=self)
        self.scaleInput = InputField(default_value='scale', limit_content_to='().,0123456789',
                                     character_limit=13, position=(0, -.15, -.01), scale=(.9, .15), parent=self)

        self.shadows = Entity(position=(-.03, -.33, -.01), parent=self)
        self.shadowsText = Text(text='shadows', position=(-.4, .035), scale=3, parent=self.shadows)
        self.shadowsBox = CheckBox(scale=.08, parent=self.shadows)

    def update_line(self):
        ConnectorLine(runButton, self.texture_attachment)

    def make(self):
        self.m = Entity(model=self.path.text)

    def undo(self):
        destroy(self.m, delay=0)


class ColorNode(Draggable):
    def __init__(self, text='RGB Color', position=(0, 0), scale=(.35, .3), color=Color(0, 0, 0, 0.72)):
        super().__init__(text=text, text_origin=(0, .4), position=position, scale=scale,
                         radius=0.05, color=color,
                         highlight_color=color)

        self.output_attachment = Button(model='circle', position=(.5, -.2, -.01), scale=.07, parent=self)

        self.slider_r = Slider(0, 255, position=(-0.475, .2, -.01), scale=(1.9, 2), parent=self,
                               dynamic=True,
                               on_value_changed=self.UpdateColor)
        self.slider_g = Slider(0, 255, position=(-0.475, .1, -.01), scale=(1.9, 2), parent=self,
                               dynamic=True,
                               on_value_changed=self.UpdateColor)
        self.slider_b = Slider(0, 255, position=(-0.475, 0, -.01), scale=(1.9, 2), parent=self,
                               dynamic=True,
                               on_value_changed=self.UpdateColor)

        self.value_text = Text(align="left", position=(-0.44, -.1, -.01), size=.065, parent=self)

        self.preview = Entity(model="cube", position=(-0, -.35, -.01), scale=(0.55, 0.22), parent=self)

    def make(self):
        print(self.color)

    def UpdateColor(self):
        self.value_text.text = (
        round(self.slider_r.value, 2), round(self.slider_g.value, 2), round(self.slider_b.value, 2), 0.72)
        self.preview.color = color.rgba(self.slider_r.value, self.slider_g.value, self.slider_b.value, 255)

    def undo(self):
        destroy(self, delay=0)


class DirectionalLightNode(Draggable):
    def __init__(self, text='Directional Light', position=(0, 0), scale=.3, color=Color(0, 0, 0, 0.72)):
        super().__init__(
            text=text,
            text_origin=(0, .4),
            position=position,
            scale=scale,
            radius=0.05,
            color=color,
            highlight_color=color)

        self.shadows = Entity(position=(-.03, .15, -.01), parent=self)
        self.shadowsText = Text(text='shadows', position=(-.4, .035), scale=3, parent=self.shadows)
        self.shadowsBox = CheckBox(scale=.08, parent=self.shadows)

        self.resolutionText = Text(text='shadows resolution', position=(-.4, -.052), scale=3, parent=self.shadows)

        self.MapResolutionSlider = Slider(32, 2048, default=256, step=32, position=(-0.475, -.1), scale=(1.9, 2),
                                          parent=self,
                                          dynamic=True)

    def make(self):
        self.sun = DirectionalLight(shadows=self.shadowsBox.state)
        self.sun.look_at(Vec3(1, -1, -1))
        self.sun.shadow_map_resolution = Vec2(self.MapResolutionSlider.value, self.MapResolutionSlider.value)

    def undo(self):
        destroy(self.sun, delay=0)


class CameraNode(Draggable):
    def __init__(self, text='Camera Type Name', position=(0, 0), scale=.3, color=Color(0, 0, 0, 0.75), **kwargs):
        super().__init__(
            text=text,
            text_origin=(0, .4),
            position=position,
            scale=scale,
            radius=.05,
            color=color,
            highlight_color=color)

        self.camera = Entity(position=(-.03, .15, -.01), scale=(0.3, 0.05), parent=self)

        Entity(parent=self, model="plane", position=(0, 0, 1), rotation=(0, 0, 0), scale=(0.3, 0.05),
               color=Color(255, 0, 0, 0.90))

        # self.cameraText = Text(text='Camera Type Name', position=(-.43, .04, -.01), scale=3.25, parent=self)
        Text(text="Editor Camera", position=(-0.25, .2, -.02), scale=3, parent=self)
        self.ec_checkbox = CheckBox(position=(0, .08, -.02), scale=.08, parent=self)

        Text(text="First Camera", position=(-0.25, 0, -.02), scale=3, parent=self)
        self.fpc_checkbox = CheckBox(position=(0, -.14, -.02), scale=.08, parent=self)

    def make(self):
        if self.ec_checkbox.state is True:
            EditorCamera()
        elif self.fpc_checkbox is True:
            FirstPersonController()
        else:
            camera.position = (0, 0, 0)
            camera.rotation = (0, 0, 0)

    def undo(self):
        destroy(self, delay=0)


nodes = []


def createNode(node):
    newNode = node()
    nodes.append(newNode)


def save_project():
    wp = FileBrowserSave(file_type='.json', z=-5)

    import json
    save_data = {
        "nodes": {
            "node1": {
                "model": nodes
            }
        }
    }

    print(nodes)
    wp.data = json.dumps(save_data)


def convert():
    try:
        print(nodes)
        print(scene.entity)
    except Exception as e:
        print_warning(f"Error: {e}")


DropdownMenu(text='File', buttons=(
    DropdownMenuButton(text='New'),
    DropdownMenuButton(text='Open'),
    DropdownMenuButton(text='Save', on_click=save_project),
    DropdownMenu(text='Options', buttons=(
        DropdownMenuButton(text='Option a'),
        DropdownMenuButton(text='Option b'),
    )),
    DropdownMenuButton(text='Convert', color=color.rgb(0, 100, 0), on_click=convert),
    DropdownMenuButton(text='Exit', color=color.rgb(75, 0, 0), on_click=application.quit),
))

# Add
addMenu = DropdownMenu(text='Add', buttons=(
    DropdownMenuButton(text='Model', on_click=Func(createNode, ModelNode)),
    DropdownMenuButton(text='Light', on_click=Func(createNode, DirectionalLightNode)),
    DropdownMenuButton(text='Color', on_click=Func(createNode, ColorNode)),
    DropdownMenuButton(text='Camera', on_click=Func(createNode, CameraNode)),
))

addMenu.x = window.top_left.x + .23


def run():
    camera.ui.disable()
    backButton.visible = True
    for i in range(len(nodes)):
        nodes[i].make()


def back():
    camera.ui.enable()
    backButton.visible = False


def input(key):
    if held_keys['control'] and key == "e":
        try:
            camera.ui.enable()
            for i in range(len(nodes)):
                nodes[i].undo()
        except AttributeError:
            print_on_screen(text=f"Please use a CAMERA !", position=(-.1, 0), scale=2)

    if held_keys['control'] and key == "w":
        try:
            if nodes:
                cube = nodes.pop()
                destroy(cube)

                print_on_screen(text=f"{cube} was deleted !", position=(-.1, 0), scale=2)
        except AssertionError:
            print_on_screen(text="Try Again !", position=(-.1, 0), scale=2)

    if held_keys['control'] and key == 'scroll up':
        for node in nodes:
            if node.scale < 0.89:
                node.scale = node.scale * 1.2

    if held_keys['control'] and key == 'scroll down':
        for node in nodes:
            if node.scale > 0.12:
                node.scale = node.scale / 1.2

    if held_keys['delete']:
        if nodes:
            node = nodes.pop()
            destroy(node)

    print(key)


# grid = Entity(model=Grid(50, 50), rotation=(0, 0, 0), scale=(50, 50), position=(0, 0, 20))

runButton = Button(model='circle', icon='../icons/run.png', position=window.top_right + (-.025, -.025), scale=.03,
                   color=color.black10,
                   on_click=run)

backButton = Button(parent=scene, model='circle', icon='../icons/run.png', position=window.top_right + (-.025, -.025),
                    scale=1,
                    rotation=(0, 0, 180),
                    color=color.black10,
                    visible=False,
                    on_click=back)

app.run()
