import json
from PIL import Image
from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenuButton, DropdownMenu
from ursina.prefabs.file_browser import FileBrowser
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.prefabs.grid_editor import PixelEditor
from ursina.prefabs.health_bar import HealthBar
from ursina.prefabs.video_recorder import VideoRecorderUI

app = Ursina(size=(720, 480))
window.fullscreen = False
window.borderless = False
window.exit_button.enabled = False
window.fps_counter.enabled = False

base = application.base

editor_camera = EditorCamera()

project_name = 'Scene1'
name = 'Entity1'
cube_nmb = []
lock_x = 0
lock_y = 0
lock_z = 0

empty_texture = Texture(Image.new(mode='RGBA',
                                      size=(32, 32),
                                      color=(255, 255, 255, 255)))
pe = PixelEditor(texture=empty_texture, brush_size=1, z=-2)
pe.visible = False
pe.enabled = False


def hide_w():
    destroy(wp)


def add():
    def hide_w():
        destroy(wp)

    def cube():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cube1 = Draggable(parent=scene, model='cube', name=f'Cube{len(cube_nmb)}', postion=(0, 0, 0), color=rgb(r, g, b), texture='new_texture',
                          lock=(lock_z, lock_y, lock_x))
        mesh_axis_x = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.red, rotation=(0, 0, 0), z=-1)
        mesh_axis_y = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.green, rotation=(0, 90, 0), x=-1)
        mesh_axis_z = Button(parent=cube1, model='cube', scale=(0.05, 1, 0.05), color=color.blue, rotation=(0, 90, 0), y=1)
        cube_nmb.append(cube1)
        destroy(wp)

    def sphere():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cube1 = Draggable(parent=scene, model='sphere', name=f'Sphere{len(cube_nmb)}', postion=(0, 0, 0), color=rgb(r, g, b),
                          lock=(lock_z, lock_y, lock_x))
        mesh_axis_x = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.red, rotation=(0, 0, 0), z=-1)
        mesh_axis_y = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.green, rotation=(0, 90, 0), x=-1)
        mesh_axis_z = Button(parent=cube1, model='cube', scale=(0.05, 1, 0.05), color=color.blue, rotation=(0, 90, 0), y=1)
        cube_nmb.append(cube1)
        destroy(wp)

    def plane():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cube1 = Draggable(parent=scene, model='plane', name=f'Plane{len(cube_nmb)}', postion=(0, 0, 0), color=rgb(r, g, b),
                          lock=(lock_z, lock_y, lock_x))
        mesh_axis_x = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.red, rotation=(0, 0, 0), z=-1)
        mesh_axis_y = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.green, rotation=(0, 90, 0), x=-1)
        mesh_axis_z = Button(parent=cube1, model='cube', scale=(0.05, 1, 0.05), color=color.blue, rotation=(0, 90, 0), y=1)
        cube_nmb.append(cube1)
        destroy(wp)

    def quad():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cube1 = Draggable(parent=scene, model='cube', name=f'Quad{len(cube_nmb)}', postion=(0, 0, 0), color=rgb(r, g, b),
                          lock=(lock_z, lock_y, lock_x))
        mesh_axis_x = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.red, rotation=(0, 0, 0), z=-1)
        mesh_axis_y = Button(parent=cube1, model='cube', scale=(0.05, 0.05, 1), color=color.green, rotation=(0, 90, 0), x=-1)
        mesh_axis_z = Button(parent=cube1, model='cube', scale=(0.05, 1, 0.05), color=color.blue, rotation=(0, 90, 0), y=1)
        cube_nmb.append(cube1)
        destroy(wp)

    def mesh():
        def hide_cm():
            destroy(cm)

        def create_mesh():
            verts = input1.text
            tris = input2.text
            uvs = input3.text
            norms = input4 * len(verts)
            colors = (color.red, color.blue, color.lime, color.black)
            e = Entity(model=Mesh(vertices=verts, triangles=tris, uvs=uvs, normals=norms, colors=colors), scale=2)

        destroy(wp)
        verts = ((0, 0, 0), (1, 0, 0), (.5, 1, 0), (-.5, 1, 0))
        tris = (1, 2, 0, 2, 3, 0)
        uvs = ((1.0, 0.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0))
        norms = ((0, 0, -1),) * len(verts)

        input1 = InputField(character_limit=50)
        input2 = InputField(character_limit=40)
        input3 = InputField(character_limit=40)
        input4 = InputField(character_limit=40)
        cm = WindowPanel(
            title='Mesh',
            content=(
                Text('Mesh Type:'),
                Text(text='Vertices:'),
                input1,
                Text(text='Triangles:'),
                input2,
                Text(text='UVS:'),
                input3,
                Text(text='Normals:'),
                input4,
                Button(text='Create', color=color.azure, on_click=create_mesh),
                Button(text='Close', color=color.red, on_click=hide_cm)
            ),
        )

    wp = WindowPanel(
        title='Model',
        content=(
            Text('Model Type:'),
            Button(text='Cube', color=color.azure, on_click=cube),
            Button(text='Sphere', color=color.azure, on_click=sphere),
            Button(text='Plane', color=color.azure, on_click=plane),
            Button(text='Quad', color=color.azure, on_click=quad),
            Button(text='Mesh', color=color.azure, on_click=mesh),
            Button(text='Close', color=color.red, on_click=hide_w)
        ),
    )
    print(len(cube_nmb))


def remove_btn():
    global cube1
    for cube1 in cube_nmb:
        cube_nmb.remove(cube1)
        destroy(cube1)


def set_texture():
    def hide_w():
        destroy(wp)

    def texture():
        for cube1 in cube_nmb:
            cube1.texture = texture_name.text

    texture_name = InputField(text='new_texture')

    wp = WindowPanel(
        title='Texture',
        content=(
            Text('Texture Path:'),
            texture_name,
            Button(text='Submit', color=color.azure, on_click=texture),
            Button(text='Close', color=color.red, on_click=hide_w)
        ),
    )


def set_x():
    editor_camera.rotation = (0, 0, 0)


def set_y():
    editor_camera.rotation = (0, 90, 0)


def set_z():
    editor_camera.rotation = (90, 0, 0)


def render_image():
    base.screenshot(namePrefix=f"render_{project_name}.png", defaultFilename=0)
    print_on_screen("Render finished !", scale=2, position=(-0.1, 0))


def render_video():
    vd_rec = VideoRecorderUI()
    vd_rec.visible = True


def open_model():
    fb = FileBrowser(file_types=('.gltf', '.obj'), enabled=True)

    def on_submit(paths):
        print('--------', paths)
        for p in paths:
            print('---', p)
            model1 = Draggable(parent=scene, model=f'assets/models/zombie.gltf', color=color.blue, scale=(2, 2, 2), position=(0, 0, 0))
            print(model1.model)

    fb.on_submit = on_submit


def rename_project():
    def rename_w():
        global project_name
        text = name_input.text
        if len(text) <= 9:
            project_name = text
        else:
            print_on_screen(text="Your name is too long", scale=2, position=(-0.2, 0, 0))

    def hide_w():
        destroy(wp)

    name_input = InputField(name='name_field')

    wp = WindowPanel(
        title='Rename Project',
        content=(
            Text('Name:'),
            name_input,
            Button(text='Submit', color=color.azure, on_click=rename_w),
            Button(text='Close', color=color.red, on_click=hide_w)
        ),
    )
    wp.y = wp.panel.scale_y / 2 * wp.scale_y  # center the window panel


def open_project():
    destroy(wp)
    fb = FileBrowser(file_types=('.msstd'), enabled=True, z=-5)

    def on_submit(paths):
        print('--------', paths)
        for p in paths:
            print('---', p)

            with open(f'{p}') as f:
                data = json.load(f)

            print(data)

            try:
                project_name = data['project']['name']
                editor_camera.rotation = data['project']['camera']['rotation']
                print(data['project']['name'])
                print(data['project']['camera']['rotation'])
                print(data['project']['render'])
                print(data['project']['models'])
            except:
                print_warning("Your project is corrupt !")
                print_on_screen("Your project is corrupt !", scale=2, position=(-0.3, 0))

    fb.on_submit = on_submit


def save_project():
    wp = FileBrowserSave(file_type='.msstd', z=-5)

    import json
    save_data = {
        'project': {
            'name': f'{project_name}',
            'camera': {
                'postion': f'{editor_camera.position}',
                'rotation': f'{editor_camera.rotation}'
            },
            'render': False,
            'models': f'{cube_nmb}'
        }
    }
    wp.data = json.dumps(save_data)


def texture_edit():
    def hide_pe():
        destroy(exit_button)
        pe.enabled = False
        pe.visible = False
        empty_texture.save("new_texture.png")
        axis_x.visible = True
        axis_y.visible = True
        axis_z.visible = True
        floor.visible = True

    destroy(wp)
    empty_texture = Texture(Image.new(mode='RGBA',
                                      size=(32, 32),
                                      color=(255, 255, 255, 255)))
    pe.enabled = True
    pe.visible = True
    pe.texture = empty_texture

    axis_x.visible =False
    axis_y.visible =False
    axis_z.visible =False
    floor.visible = False

    exit_button = Button(parent=camera.ui, ignore_paused=True, origin=(.5, .5), y=0.5, x=0.614,
           z=-1, scale=(.05, .025), color=color.red.tint(-.2), text='x',
           on_click=hide_pe, name='exit_button')


wp = WindowPanel(
    title='Info Project',
    content=(
        Text('Name:'),
        Button(text='General', color=color.azure, on_click=hide_w),
        Button(text='Texture Edit', color=color.azure, on_click=texture_edit),
        Button(text='SFX', color=color.azure),
        Button(text='Open', color=color.azure, on_click=open_project),
        Button(text='Close', color=color.red, on_click=hide_w)
    ),
)
wp.y = 0.3

file = DropdownMenu('File', buttons=(
    DropdownMenuButton('New'),
    DropdownMenuButton('Open', on_click=open_project),
    DropdownMenuButton('Rename Project', on_click=rename_project),
    DropdownMenuButton('Save', on_click=save_project),
    DropdownMenu('Import', buttons=(
        DropdownMenuButton('OBJ', on_click=open_model),
        DropdownMenuButton('GLTF', on_click=open_model),
    )),
    DropdownMenuButton('Exit', on_click=application.quit),
))
render = DropdownMenu('Render', buttons=(
    DropdownMenuButton('Render Image', on_click=render_image),
    DropdownMenuButton('Render Video', on_click=render_video)
))
edit = DropdownMenu('Edit', buttons=(
    DropdownMenuButton('Object Mode'),
    DropdownMenuButton('Edit Mode'),
    DropdownMenuButton('Edit Texture', on_click=texture_edit)
))
shaders = DropdownMenu('Shaders', buttons=(
    DropdownMenuButton('No Light'),
    DropdownMenuButton('With Light')
))
render.x = -0.659
edit.x = -0.43
shaders.x = -0.201


footer = Entity(parent=camera.ui, scale=(1.95, 0.3), model=Quad(aspect=3, radius=0), color=color.black33, y=-0.4)
left = Entity(parent=camera.ui, scale=(0.3, 0.9), model=Quad(aspect=3, radius=0), color=color.black50, x=0.75, y=0.2)

# Help Keybind

Text(
    text=dedent('''
               shift + a:            object panel
               ctrl + scroll up:     + size to texture brush
               ctrl + scroll down:   - size to texture brush
               ctrl + o:             open project
               ctrl + s:             save project
           '''),
    position=(-0.89, 0.39),
    scale=.75
)

# Footer
floor = Entity(model=Grid(50, 50), rotation=(90, 0, 0), scale=(50, 50))
axis_x = Entity(model='cube', scale=(0.05, 0.05, 50), color=color.red, rotation=(0, 0, 0))
axis_y = Entity(model='cube', scale=(0.05, 0.05, 50), color=color.green, rotation=(0, 90, 0))
axis_z = Entity(model='cube', scale=(0.05, 20, 0.05), color=color.blue, rotation=(0, 90, 0), y=10)

Button(parent=footer, text="Add", scale=(0.1, 0.2), radius=0, x=-0.4, y=0.25, on_click=add)
Button(parent=footer, text="Rename", scale=(0.1, 0.2), radius=0, x=-0.4, y=0)
Button(parent=footer, text="Remove", scale=(0.1, 0.2), radius=0, x=-0.4, y=-0.25, on_click=remove_btn)

button_x = Button(parent=footer, text=f"X: 0.0", scale=(0.1, 0.2), radius=0, x=-0.25, y=0.25).alpha = 0
button_y = Button(parent=footer, text=f"Y: 0.0", scale=(0.1, 0.2), radius=0, x=-0.25, y=0).alpha = 0
button_z = Button(parent=footer, text=f"Z: 0.0", scale=(0.1, 0.2), radius=0, x=-0.25, y=-0.25).alpha = 0

Button(parent=footer, text="X", scale=(0.1, 0.2), radius=0, x=-0.15, y=0.25, on_click=set_x)
Button(parent=footer, text="Y", scale=(0.1, 0.2), radius=0, x=-0.15, y=0, on_click=set_y)
Button(parent=footer, text="Z", scale=(0.1, 0.2), radius=0, x=-0.15, y=-0.25, on_click=set_z)


# Left

Text(parent=left, text='Project Info', scale=(3, 1.5), x=-0.22, y=0.33, z=-1)

project_text = Text(parent=left, text=f'Project Name: {project_name}', scale=(2.5, 1), x=-0.5, y=0.23, z=-1)

Text(parent=left, text='Camera Info', scale=(3, 1.5), x=-0.20, y=0.2, z=-1)
camera_text = Text(parent=left, text=f'Camera Position: {camera.position}', scale=(2.5, 1), x=-0.5, y=0.13, z=-1)
camera_rotation = Text(parent=left, text=f'Camera Position: {camera.rotation}', scale=(2.5, 1), x=-0.5, y=0.1, z=-1)

Text(parent=left, text='Object Info', scale=(3, 1.5), x=-0.20, y=0.04, z=-1)
cube_text = Text(parent=left, text=f'Object Name: None', scale=(2.5, 1), x=-0.5, y=-0.01, z=-1)
cube_position = Text(parent=left, text=f'Object Position: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.04, z=-1)
cube_scale = Text(parent=left, text=f'Object Scale: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.07, z=-1)
cube_texture = Text(parent=left, text=f'Object Texture: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.1, z=-1)


origin = Entity(model='quad', color=color.orange, scale=(.05, .05))
slider = Slider(0, 250, text='Timeline', default=0, height=Text.size*2, width=Text.size*8, y=-.4, step=1, vertical=False)
runnig = False


def input(key):
    global lock_x, lock_y, lock_z, runnig
    print(key)
    if key == '0':
        lock_x = 0
        lock_y = 0
        lock_z = 0
    if key == '1':
        lock_x = 1
        lock_y = 0
        lock_z = 0
    if key == '2':
        lock_y = 1
        lock_x = 0
        lock_z = 0
    if key == '3':
        lock_z = 1
        lock_y = 0
        lock_x = 0

    if held_keys['shift'] and key == "q":
        add()
    if held_keys['shift'] and key == "t":
        set_texture()
    if held_keys['control'] and key == "s":
        save_project()
    if held_keys['control'] and key == "o":
        open_project()

    if held_keys['control'] and key == 'scroll up':
        pe.brush_size += 1
        print(pe.brush_size)

    if not pe.brush_size <= 1:
        if held_keys['control'] and key == 'scroll down':
            pe.brush_size -= 1
            print(pe.brush_size)

    if held_keys['space']:
        if runnig is False:
            runnig = True
            slider.value += 1
            editor_camera.z = -slider.value
        else:
            runnig = False

    if held_keys['left arrow']:
        slider.value -= 1

    if held_keys['right arrow']:
        slider.value += 1


def update():
    for cube1 in cube_nmb:
        cube1.lock = (lock_z, lock_y, lock_x)
        if mouse.hovered_entity == cube1:
            print(cube1.name)
            cube_text.text = f'Object Name: {cube1.name}'
            cube_position.text = f'Object Position: {round(cube1.x, 2)}, {round(cube1.y, 2)}, {round(cube1.z, 2)}'
            cube_scale.text = f'Object Scale: {round(cube1.scale_x, 2)}, {round(cube1.scale_y, 2)}, {round(cube1.scale_z, 2)}'
            cube_texture.text = f'Object Texture: {cube1.texture}'

    if held_keys['s']:
        for cube1 in cube_nmb:
            if mouse.hovered_entity == cube1:
                cube1.scale = (mouse.x * 10, mouse.y * 10, mouse.x * 10)

    project_text.text = f'Project Name: {project_name}'
    camera_text.text = f'Camera Position: {round(camera.position)}'
    camera_rotation.text = f'Camera Rotation: X: {round(editor_camera.rotation_x)} Y: {round(editor_camera.rotation_y)} Z: {round(editor_camera.rotation_z)}'


app.run()
