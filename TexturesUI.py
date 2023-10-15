from ursina import *
from ursina.shaders.screenspace_shaders.pixelation_shader import pixelation_shader

app = Ursina(size=(720, 480))
window.fullscreen = False
window.borderless = False
window.exit_button.enabled = False
window.fps_counter.enabled = False


def test(txt_arg: str):
    cube.texture = txt_arg
    sphere.texture = txt_arg


button_dict = {}

bl = ButtonList(button_dict, font='VeraMono.ttf', button_height=1.5, popup=True)

bl.button_dict = {
            'noise': Func(test, 'noise'),
            'grass': Func(test, 'grass'),
            'vignette': Func(test, 'vignette'),
            'arrow_right': Func(test, 'arrow_right'),
            'test_tileset': Func(test, 'test_tileset'),
            'tilemap_test_level': Func(test, 'tilemap_test_level'),
            'shore': Func(test, 'shore'),
            'file_icon': Func(test, 'file_icon'),
            'sky_sunset': Func(test, 'sky_sunset'),
            'radial_gradient': Func(test, 'radial_gradient'),
            'circle': Func(test, 'circle'),
            'perlin_noise': Func(test, 'perlin_noise'),
            'brick': Func(test, 'brick'),
            'grass_tintable': Func(test, 'grass_tintable'),
            'circle_outlined': Func(test, 'circle_outlined'),
            'ursina_logo': Func(test, 'ursina_logo'),
            'arrow_down': Func(test, 'arrow_down'),
            'cog': Func(test, 'cog'),
            'vertical_gradient': Func(test, 'vertical_gradient'),
            'white_cube': Func(test, 'white_cube'),
            'horizontal_gradient': Func(test, 'horizontal_gradient'),
            'folder': Func(test, 'folder'),
            'rainbow': Func(test, 'rainbow'),
            'heightmap_1': Func(test, 'heightmap_1'),
            'sky_default': Func(test, 'sky_default'),
}

cube = Entity(model="cube", scale=(1, 1, 1), x=-4, y=1)
sphere = Entity(model="sphere", scale=(1, 1, 1), x=-4, y=-1)

Entity(model="quad", scale=(999, 999), color=color.black66, z=999)


def update():
    cube.rotation_y += 1
    cube.rotation_x += 1

    sphere.rotation_y += 1
    sphere.rotation_x += 1


app.run()
