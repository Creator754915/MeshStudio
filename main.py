import json

from PIL import Image
from ursina import *
from ursina import Entity
from ursina.prefabs.dropdown_menu import DropdownMenuButton, DropdownMenu
from ursina.prefabs.file_browser import FileBrowser
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.prefabs.grid_editor import PixelEditor
from ursina.prefabs.video_recorder import VideoRecorderUI
from ursina.shaders import lit_with_shadows_shader
from assets.plugins.ClickPanel import ClickPanel

from sun import Sun

window.title = "MeshStudio"
window.icon = "meshstudio_logo.png"
app = Ursina(size=(720, 480))
window.fullscreen = False
window.borderless = False
window.exit_button.enabled = False
window.fps_counter.enabled = False

editor_camera = EditorCamera()
sky = Sky(texture="sky_default")
cameraEntity = Entity(model="camera.obj", scale=0.5, wireframe=True, rotation=(0, 0, 40), position=(-8, 5, 0))

project_name = 'Scene1'
name = 'Entity1'
cube_nmb = []
lock_xyz = (0, 0, 0)

timeline_speed = 1

empty_texture = Texture(Image.new(mode='RGBA',
                                  size=(32, 32),
                                  color=(255, 255, 255, 255)))
pe = PixelEditor(texture=empty_texture, brush_size=1, z=-2, visible=False, enabled=False)
pe.help_text.visible = False


def hide_w():
    destroy(wp)


def add():
    def hide_wp():
        destroy(wp)

    def entity_cube(model_t):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        cube1 = Draggable(parent=scene, model=model_t, name=f'Cube{len(cube_nmb)}', collider="box",
                          postion=(0, 0, 0),
                          color=rgb(r, g, b), texture='white_cube',
                          lock=(0, 0, 0))
        # cube1.plane_direction = (1, 0, 0)

        Button(parent=cube1, model='arrow', collider="box", scale=1.2, color=color.red, rotation=(0, 90, 0), z=-0.5)
        Button(parent=cube1, model='arrow', collider="box", scale=1.2, color=color.green, rotation=(0, 180, 0), x=-0.5)
        Button(parent=cube1, model='arrow', collider="box", scale=1.2, color=color.blue, rotation=(0, 0, -90), y=0.5)

        cube_nmb.append(cube1)
        destroy(wp)

    def mesh():
        def hide_cm():
            destroy(cm)

        def create_mesh():
            try:
                verts = input1.text
                tris = input2.text
                uvs = input3.text
                norms = input4 * len(verts)

                # verts = ((0, 0, 0), (1, 0, 0), (.5, 1, 0), (-.5, 1, 0))
                # tris = (1, 2, 0, 2, 3, 0)
                # uvs = ((1.0, 0.0), (0.0, 1.0), (0.0, 0.0), (1.0, 1.0))
                # norms = ((0, 0, -1),) * len(verts)

                colors = (color.red, color.blue, color.lime, color.black)
                e = Entity(model=Mesh(vertices=verts, triangles=tris, uvs=uvs, normals=norms, colors=colors), scale=2)
            except:
                print_warning("Error: Failed to create the Mesh")

        destroy(wp)

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
        cm.y = cm.panel.scale_y / 2 * cm.scale_y

    wp = WindowPanel(
        title='Model',
        content=(
            Text('Model Type:'),
            Button(text='Cube', color=color.azure, on_click=Func(entity_cube, "cube")),
            Button(text='Sphere', color=color.azure, on_click=Func(entity_cube, "sphere")),
            Button(text='Plane', color=color.azure, on_click=Func(entity_cube, "plane")),
            Button(text='Quad', color=color.azure, on_click=Func(entity_cube, "quad")),
            Button(text='Mesh', color=color.azure, on_click=mesh),
            Button(text='Close', color=color.red, on_click=hide_wp)
        ),
    )

    wp.y = wp.panel.scale_y / 2 * wp.scale_y

    print(len(cube_nmb))


def rename_object():
    def hide_wp():
        destroy(wp)

    object_name = InputField(text='Object1')

    def chg_name():
        for cube in cube_nmb:
            cube.name = object_name.text

    wp = WindowPanel(
        title='Object Name',
        content=(
            Text('New Object Name:'),
            object_name,
            Button(text='Submit', color=color.azure, on_click=chg_name),
            Button(text='Close', color=color.red, on_click=hide_wp)
        ),
    )

    wp.y = wp.panel.scale_y / 2 * wp.scale_y


def remove_cube(*args):
    def all_cube():
        for cube in cube_nmb:
            destroy(cube)

    if cube_nmb:
        cube = cube_nmb.pop()
        destroy(cube)

    if args == 'all_cube':
        all_cube()


def set_texture():
    def hide_tw():
        destroy(tw)

    def textures():
        if cube_nmb:
            cube = cube_nmb[:-1]
            cube.texture = texture_name.text

    texture_name = InputField(text='new_texture')

    tw = WindowPanel(
        title='Texture',
        content=(
            Text('Texture Path:'),
            texture_name,
            Button(text='Submit', color=color.azure, on_click=textures),
            Button(text='Close', color=color.red, on_click=hide_tw)
        ),
    )

    tw.y = tw.panel.scale_y / 2 * tw.scale_y


def open_sound_editor():
    print("Coming soon...")


def set_x():
    editor_camera.rotation = (0, 0, 0)


def set_y():
    editor_camera.rotation = (0, 90, 0)


def set_z():
    editor_camera.rotation = (90, 0, 0)


def render_image():
    # base = application.base

    # editor_camera.position = 0, 5, -24

    # base.screenshot(namePrefix=f"render_{project_name}.png", defaultFilename=0)
    # print_on_screen("Render finished !", scale=2, position=(-0.1, 0))
    # editor_camera.enabled = False

    editor_camera.world_position = (cameraEntity.x, cameraEntity.y, 0)
    editor_camera.rotation = (cameraEntity.rotation_z, 90, 0)


def render_video():
    vd_rec = VideoRecorderUI()
    vd_rec.visible = True


def open_model_obj():
    fb = FileBrowser(file_types='.obj', enabled=True)

    def on_submit(paths):
        print('--------', paths)
        for p in paths:
            print('---', p)
            model1 = load_model(p, use_deepcopy=True)
            print(model1.model)

    fb.on_submit = on_submit


def open_model_gltf():
    fb = FileBrowser(file_types='.gltf', enabled=True)

    def on_submit(paths):
        print('--------', paths)
        for p in paths:
            print('---', p)
            model1 = load_model(p.name, use_deepcopy=True)
            print(model1)

    fb.on_submit = on_submit


def rename_project():
    def hide_wp():
        destroy(wp)

    def rename_w():
        global project_name
        new_project_name = name_input.text
        if len(new_project_name) <= 9:
            project_name = new_project_name
        else:
            print_on_screen(text="Your name is too long", scale=2, position=(-0.2, 0, 0))

    name_input = InputField(name='name_field')

    wp = WindowPanel(
        title='Rename Project',
        content=(
            Text('Name:'),
            name_input,
            Button(text='Submit', color=color.azure, on_click=rename_w),
            Button(text='Close', color=color.red, on_click=hide_wp)
        ),
    )
    wp.y = wp.panel.scale_y / 2 * wp.scale_y


def open_project():
    destroy(wp)
    fb = FileBrowser(file_types='.msstd', enabled=True, z=-5)

    def on_submit(paths):
        global project_name, editor_camera
        print('--------', paths)
        for p in paths:
            print('---', p)

            with open(f'{p}') as f:
                data = json.load(f)

            print(data)

            try:
                project_name = data['project']['name']

                editor_camera.rotation_x = data['project']['camera']['rotation']['x']
                editor_camera.rotation_y = data['project']['camera']['rotation']['y']
                editor_camera.rotation_z = data['project']['camera']['rotation']['z']

                print(data['project']['camera']['position']['x'])
                print(data['project']['models'])
            except json.decoder.JSONDecodeError:
                print_warning("Your project is corrupt !")
                print_on_screen("Your project is corrupt !", scale=2, position=(-0.3, 0))

    fb.on_submit = on_submit


def save_project():
    wp = FileBrowserSave(file_type='.msstd', z=-5)

    import json
    save_data = {
        "project": {
            "name": f'{project_name}',
            "camera": {
                "position": {
                    "x": editor_camera.x,
                    "y": editor_camera.y,
                    "z": editor_camera.z
                },
                "rotation": {
                    "x": 90,
                    "y": 0,
                    "z": 0
                }
            },
            "models": f'{cube_nmb}'
        }
    }
    wp.data = json.dumps(save_data)


def general_mode():
    axis_x.visible = True
    axis_y.visible = True
    axis_z.visible = True
    floor.visible = True
    footer.visible = True
    slider.visible = True
    left.visible = True


def texture_edit():
    def hide_pe():
        destroy(exit_button)
        pe.visible, pe.enabled = False, False

        empty_texture.save("new_texture.png")

        axis_x.visible = True
        axis_y.visible = True
        axis_z.visible = True
        floor.visible = True
        footer.visible = True
        slider.visible = True
        left.visible = True
        texture_scale.visible = True

    destroy(wp)
    empty_texture = Texture(Image.new(mode='RGBA',
                                      size=(32, 32),
                                      color=(255, 255, 255, 255)))

    texture_scale = TextField(parent=camera.ui, ignore_paused=True, origin=(.5, .5), y=-0.5, x=-0.614,
                              z=-1)

    pe.enabled = True
    pe.visible = True
    pe.texture = empty_texture

    axis_x.visible = False
    axis_y.visible = False
    axis_z.visible = False
    floor.visible = False
    footer.visible = False
    slider.visible = False
    left.visible = False
    texture_scale.visible = False

    exit_button = Button(parent=camera.ui, ignore_paused=True, origin=(.5, .5), y=0.5, x=0.614,
                         z=-1, scale=(.05, .025), color=color.red.tint(-.2), text='x',
                         on_click=hide_pe, name='exit_button')


def edit_mode():
    def show_vert():
        axis_x.visible = False
        axis_y.visible = False
        axis_z.visible = False
        floor.visible = False
        footer.visible = False
        slider.visible = False
        left.visible = False

        m = load_model("assets/models/cube.obj", use_deepcopy=True)
        for t in m.vertices:
            Draggable(parent=scene, model="cube", color=color.blue, scale=0.08, position=t)

    show_vert()


plane = Entity(name="plane_shaders", model='plane', scale=20, color=color.gray, shader=lit_with_shadows_shader,
               visible=False)


def shaders_active():
    global sun_l
    axis_x.visible = False
    axis_y.visible = False
    axis_z.visible = False
    floor.visible = False
    footer.visible = False
    slider.visible = False
    left.visible = False

    EditorCamera()

    plane.visible = True

    sun_l = Sun(target=origin)


def shaders_desactive():
    global sun_l
    axis_x.visible = True
    axis_y.visible = True
    axis_z.visible = True
    floor.visible = True
    footer.visible = True
    slider.visible = True
    left.visible = True

    plane.visible = False

    destroy(sun_l)


def preferences():
    def hide_wpr():
        destroy(wpr)

    def apply():
        try:
            sky.texture = sky_input.text
        except ResourceWarning:
            print_warning("ImportFailed: The texture are missing !")

    project_input = InputField()
    plugin_input = InputField()
    sky_input = InputField()

    wpr = WindowPanel(
        title='Preferences',
        content=(
            Text('Project Path'),
            project_input,
            Text('Import Plugin'),
            plugin_input,
            Text('Sky Texture Path'),
            sky_input,
            Button(text='Save', color=color.azure, on_click=apply()),
            Button(text='Close', color=color.red, on_click=hide_wpr)
        ),
    )

    wpr.y = wpr.panel.scale_y / 2 * wpr.scale_y


def timeline_options():
    def hide_wpt():
        destroy(wpt)

    def apply():
        global timeline_speed
        timeline_speed = speed_slider.value

        hide_wpt()

    step_slider = Slider(.5, 3, step=0.2)
    speed_slider = Slider(0.5, 5, step=0.5)

    wpt = WindowPanel(
        title='Timeline Options',
        content=(
            Text('Timeline Step'),
            step_slider,
            Text('Animation Speed'),
            speed_slider,
            Button(text='Apply', color=color.azure, on_click=apply),
            Button(text='Close', color=color.red, on_click=hide_wpt)
        ),
    )

    wpt.y = wpt.panel.scale_y / 2 * wpt.scale_y


wp = WindowPanel(
    title='Info Project',
    content=(
        Text('Name:'),
        Button(text='General', color=color.azure, on_click=hide_w),
        Button(text='Texture Edit', color=color.azure, on_click=texture_edit),
        Button(text='SFX', color=color.azure, on_click=open_sound_editor),
        Button(text='Open', color=color.azure, on_click=open_project),
        Button(text='Close', color=color.red, on_click=hide_w)
    ),
)
wp.y = 0.3

file = DropdownMenu('File', buttons=(
    DropdownMenuButton('New'),
    DropdownMenuButton('Open', on_click=open_project),
    DropdownMenuButton('Rename Project', on_click=rename_project),
    DropdownMenuButton('Save', color=color.rgb(0, 100, 0), on_click=save_project),
    DropdownMenu('Import', buttons=(
        DropdownMenuButton('OBJ', on_click=open_model_obj),
        DropdownMenuButton('GLTF', on_click=open_model_gltf),
    )),
    DropdownMenuButton('Preferences', on_click=preferences),
    DropdownMenuButton('Timeline Options', on_click=timeline_options),
    DropdownMenuButton('Exit', color=color.rgb(75, 0, 0), on_click=application.quit),
))
render_ui = DropdownMenu('Render', buttons=(
    DropdownMenuButton('Render Image', on_click=render_image),
    DropdownMenuButton('Render Video', on_click=render_video)
))
edit = DropdownMenu('Edit', buttons=(
    DropdownMenuButton('Object Mode', on_click=general_mode),
    DropdownMenuButton('Edit Mode', on_click=edit_mode),
    DropdownMenuButton('Edit Texture', on_click=texture_edit)
))
shaders = DropdownMenu('Shaders', buttons=(
    DropdownMenuButton('No Light', on_click=shaders_desactive),
    DropdownMenuButton('With Light', on_click=shaders_active)
))
render_ui.x = window.top_left.x + .23
edit.x = window.top_left.x + .459
shaders.x = window.top_left.x + .688

footer = Entity(parent=camera.ui, scale=(1.95, 0.3), model=Quad(aspect=3, radius=0), color=color.black33, y=-0.4)
left = Entity(parent=camera.ui, scale=(0.3, 0.9), model=Quad(aspect=3, radius=0), color=color.black50, x=0.75, y=0.2)

# Help Keybind

Text(
    text=dedent('''
               shift + a:            object panel
               ctrl + o:             open project
               ctrl + s:             save project
               ctrl + t:             set texture
           '''),
    position=(-0.89, 0.39),
    scale=.75,
    visible=False
)

# Footer
floor = Entity(model=Grid(1000, 1000), rotation_x=90, scale=1000, color=rgb(220, 220, 220))
axis_y = Entity(model=Mesh(vertices=[Vec3(0, 1000, 0), Vec3(0, -1000, 0)], mode='line', thickness=8),
                color=rgb(220, 0, 0))
axis_x = Entity(model=Mesh(vertices=[Vec3(1000, 0, 0), Vec3(-1000, 0, 0)], mode='line', thickness=8),
                color=rgb(0, 220, 0))
axis_z = Entity(model=Mesh(vertices=[Vec3(0, 0, 1000), Vec3(0, 0, -1000)], mode='line', thickness=8),
                color=rgb(0, 0, 220))

Button(parent=footer, text="Add", scale=(0.1, 0.2), radius=0, x=-0.4, y=0.25, on_click=add)
Button(parent=footer, text="Rename", scale=(0.1, 0.2), radius=0, x=-0.4, y=0, on_click=rename_object)
Button(parent=footer, text="Remove", scale=(0.1, 0.2), radius=0, x=-0.4, y=-0.25, on_click=remove_cube)

button_x = Button(parent=footer, text=f"Select All", scale=(0.1, 0.2), radius=0, x=-0.27, y=0.25,
                  on_click=Func(remove_cube, 'all_cube'))
button_y = Button(parent=footer, text=f"Y: 0.0", scale=(0.1, 0.2), radius=0, x=-0.27, y=0)
button_z = Button(parent=footer, text=f"Z: 0.0", scale=(0.1, 0.2), radius=0, x=-0.27, y=-0.25)

Button(parent=footer, text="X", scale=(0.1, 0.2), radius=0, x=-0.15, y=0.25, on_click=set_x)
Button(parent=footer, text="Y", scale=(0.1, 0.2), radius=0, x=-0.15, y=0, on_click=set_y)
Button(parent=footer, text="Z", scale=(0.1, 0.2), radius=0, x=-0.15, y=-0.25, on_click=set_z)

slider = Slider(1, 359, text='Timeline', default=0, height=Text.size * 2, width=Text.size * 8, y=-.4, step=1,
                vertical=False)

Button(model='cube', parent=footer, texture="icons/icon_keyframes.png", scale=(.03, 0.2), x=0.3)

# Left

Text(parent=left, text='Project Info', scale=(3, 1.5), x=-0.22, y=0.33, z=-1)

project_text = Text(parent=left, text=f'Project Name: {project_name}', scale=(2.5, 1), x=-0.5, y=0.23, z=-1)

Text(parent=left, text='Camera Info', scale=(3, 1.5), x=-0.20, y=0.2, z=-1)
camera_text = Text(parent=left, text=f'Camera Position: {camera.position}', scale=(2.5, 1), x=-0.5, y=0.13, z=-1)
camera_rotation = Text(parent=left, text=f'Camera Position: {camera.rotation}', scale=(2.5, 1), x=-0.5, y=0.1, z=-1)

Text(parent=left, text='Object Info', scale=(3, 1.5), x=-0.20, y=0.04, z=-1)
cube_text = Text(parent=left, text=f'Object Name: None', scale=(2.5, 1), x=-0.5, y=-0.01, z=-1)
cube_position = Text(parent=left, text=f'Object Position: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.04, z=-1)
cube_rotation = Text(parent=left, text=f'Object Rotation: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.07, z=-1)
cube_scale = Text(parent=left, text=f'Object Scale: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.1, z=-1)
cube_texture = Text(parent=left, text=f'Object Texture: 0, 0, 0', scale=(2.5, 1), x=-0.5, y=-0.125, z=-1)

origin = Entity(model='quad', color=color.orange, scale=(.05, .05))
runnig = False


def input(key):
    global lock_xyz
    # if key == '0':
    #     lock_xyz = (0, 0, 0)
    # if key == '1':
    #     lock_xyz = (1, 0, 0)
    # if key == '2':
    #     lock_xyz = (0, 1, 0)
    # if key == '3':
    #     lock_xyz = (0, 0, 1)

    if held_keys['shift'] and key == "q":
        add()
    if held_keys['shift'] and key == "t":
        set_texture()
    if held_keys['control'] and key == "s":
        save_project()
    if held_keys['control'] and key == "o":
        open_project()
    if held_keys['control'] and key == "x":
        remove_cube()

    if held_keys['control'] and key == 'scroll up':
        pe.brush_size += 1
        print(pe.brush_size)

    if not pe.brush_size <= 1:
        if held_keys['control'] and key == 'scroll down':
            pe.brush_size -= 1
            print(pe.brush_size)

    if held_keys['space']:
        editor_camera.rotation_x = 27
        if slider.value == 359:
            print_on_screen("FINISH")
        else:
            slider.value += timeline_speed
            editor_camera.rotation_y += -timeline_speed

    if held_keys['left arrow']:
        for cube in cube_nmb:
            cube.rotation_y -= 1

    if held_keys['right arrow']:
        for cube in cube_nmb:
            cube.rotation_y += 0.5

    if held_keys['up arrow']:
        for cube in cube_nmb:
            cube.rotation_x -= 1

    if held_keys['down arrow']:
        for cube in cube_nmb:
            cube.rotation_x += 1


rot = False

rot_x = Entity(model=Circle(14, mode='line', thickness=8), scale=(1.5, 1.5, 1.5),
               color=color.red,
               position=(0, 0, 0),
               rotation=(0, 90, 0),
               visible=False)
rot_y = Entity(model=Circle(14, mode='line', thickness=8), scale=(1.5, 1.5, 1.5),
               color=color.green,
               position=(0, 0, 0),
               rotation=(0, 0, 0),
               visible=False)
rot_z = Entity(model=Circle(14, mode='line', thickness=8), scale=(1.5, 1.5, 1.5),
               color=color.blue,
               position=(0, 0, 0),
               rotation=(90, 0, 0),
               visible=False)

ClickPanel(key_control=True, key_bind="right mouse", button_text="Add", button2_text="Remove", button3_text="Rename",
           button4_text="Copy", button5_text="Paste", button6_text="Exit")


def update():
    global lock_xyz, rot

    for cube in cube_nmb:
        # cube1.lock = lock_xyz
        if mouse.hovered_entity == cube:
            print(cube.name)
            cube_text.text = f'Object Name: {cube.name}'
            cube_position.text = f'Object Position: {round(cube.x, 2)}, {round(cube.y, 2)}, {round(cube.z, 2)}'
            cube_rotation.text = f'Object Rotation: {round(cube.rotation_x, 2)}, {round(cube.rotation_y, 2)}, {round(cube.rotation_z, 2)} '
            cube_scale.text = f'Object Scale: {round(cube.scale_x, 2)}, {round(cube.scale_y, 2)}, {round(cube.scale_z, 2)}'
            cube_texture.text = f'Object Texture: {cube.texture}'

            # tooltip_test = Tooltip(
            #    f'''<scale:1.2><gray> {cube.name} <scale:1>
            #    Scale: {cube.scale}
            #    Position: {cube.position}
            # ''',
            #    background_color=color.black33,
            #    font='VeraMono.ttf',
            #    wordwrap=30,
            # )
            # cube.tooltip = tooltip_test

    if held_keys['s']:
        for cube in cube_nmb:
            if mouse.hovered_entity == cube:
                cube.scale = (mouse.x * 50, mouse.y * 10, mouse.x * 10)

    if held_keys['r']:
        for cube in cube_nmb:
            if mouse.hovered_entity == cube and rot is False:
                rot_x.visible, rot_x.parent = True, cube
                rot_y.visible, rot_y.parent = True, cube
                rot_z.visible, rot_z.parent = True, cube
                rot = True

            else:
                rot_x.visible = False
                rot_y.visible = False
                rot_z.visible = False
                rot = False

    if editor_camera.z < -622800000:
        editor_camera.z = -500000000

    project_text.text = f'Project Name: {project_name}'
    camera_text.text = f'Camera Position: {round(camera.x)}, {round(camera.y)}, {round(camera.z)}'
    camera_rotation.text = f'Camera Rotation: X: {round(editor_camera.rotation_x)} Y: {round(editor_camera.rotation_y)} Z: {round(editor_camera.rotation_z)} '


app.run()
