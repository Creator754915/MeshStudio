from ursina import *
from ObjectOriented.WorldDirectionBox import DirectionBox
from Prefabs.additive_function import MultiFunctionCaller, TextToVar
from ObjectOriented.Gizmo.GizmoManager import GizmoManager
from ObjectOriented.ColorMenu import ColorMenu


class SceneEditor(Entity):
    def __init__(self):
        super().__init__()
        self.EditorCamera = EditorCamera()
        self.sky = Sky(texture="sky_default")

        self.GizmoManager: GizmoManager = GizmoManager()

        self.AddObjectTextList = ["Add static object", "Add dynamic object", "Add FPC", "Add TPC", "Add abstraction"]
        self.AddObjectOnClickFuncList = [self.AddEntityInScene, self.AddEntityInScene, self.AddEntityInScene,
                                         self.AddEntityInScene, self.AddEntityInScene]
        self.BasicFunctions = ["Name: ", "Parent: ", "Position x: ", "Position y: ", "Position z: ", "Rotation x: ",
                               "Rotation y: ", "Rotation z: ", "Scale x: ", "Scale y: ", "Scale z: ", "Color: ",
                               "Model: ", "Texture: ", "Texture scale: "]
        self.SpecialFunctions: dict = {
            "Color: ": lambda Obj, Parent, i: ColorMenu(Obj, (2.5, 15), BGPos=(1, 1, 0), scale=(.5, .05), parent=Parent,
                                                        y=-i * 0.08 + .34, z=-20, x=.13, radius=1).SetUp()}

        self.SpecialExtractingMethods: dict = {"Parent: ": (
            lambda Field: setattr(Field.Obj, "parent", scene), lambda Filed: ...,
            lambda Field: (getattr(Field.Obj.parent, "name")),
            "1234567890qwertyuiopasdfghklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_", True),
            "Name: ": (
                lambda Field: setattr(Field.Obj, 'name', Field.text), lambda Field: ...,
                lambda Field: (getattr(Field.Obj, "name")),
                "1234567890qwertyuiopasdfghklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_", True),
            "Model: ": (
                lambda Field: setattr(Field.Obj, 'model', Field.text), lambda Field: ...,
                lambda Field: (getattr(Field.Obj.model, "name")),
                "1234567890qwertyuiopasdfghklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_./({[]})",
                True),
            "Texture: ": (lambda Field: setattr(Field.Obj, 'texture', Field.text),
                          lambda Field: ...,
                          lambda Field: getattr(Field.Obj, "texture"),
                          "1234567890qwertyuiopasdfghklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_./({[]})",
                          True),
            "Texture scale: ": (
                lambda Field: setattr(Field.Obj, 'texture_scale', eval(Field.text)),
                lambda Field: setattr(Field, 'text', str(Field.Obj.texture_scale)),
                lambda Field: getattr(Field.Obj, "texture_scale"), "1234567890()Vec.,",
                True),
            "Position x: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "position",
                     Vec3(eval(Filed.text), Filed.Obj.position_y,
                          Filed.Obj.position_z)), self.GizmoManager.GoToEntity),
                             lambda Field: setattr(Field, "text",
                                                   str(Field.Obj.position_x)),
                             lambda Filed: str(getattr(Filed.Obj, "position_x")),
                             "1234567890.-", False),
            "Position y: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "position",
                     Vec3(Filed.Obj.position_x, eval(Filed.text),
                          Filed.Obj.position_z)), self.GizmoManager.GoToEntity),
                             lambda Filed: setattr(Filed, "text",
                                                   str(Filed.Obj.position_y)),
                             lambda Filed: str(getattr(Filed.Obj, "position_y")),
                             "1234567890.-", False),
            "Position z: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "position",
                     Vec3(Filed.Obj.position_x, Filed.Obj.position_y,
                          eval(Filed.text))), self.GizmoManager.GoToEntity),
                             lambda Filed: setattr(Filed, "text",
                                                   str(Filed.Obj.position_z)),
                             lambda Filed: str(getattr(Filed.Obj, "position_z")),
                             "1234567890.-", False),

            "Rotation x: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "rotation",
                     Vec3(eval(Filed.text), Filed.Obj.rotation_y,
                          Filed.Obj.rotation_z))),
                             lambda Field: setattr(Field, "text",
                                                   str(Field.Obj.rotation_x)),
                             lambda Filed: str(getattr(Filed.Obj.rotation, "x")),
                             "1234567890.-", False),
            "Rotation y: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "rotation",
                     Vec3(Filed.Obj.rotation_x, eval(Filed.text),
                          Filed.Obj.rotation_z))),
                             lambda Filed: setattr(Filed, "text",
                                                   str(Filed.Obj.rotation_y)),
                             lambda Filed: str(getattr(Filed.Obj.rotation, "y")),
                             "1234567890.-", False),
            "Rotation z: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "rotation",
                     Vec3(Filed.Obj.rotation_x, Filed.Obj.rotation_y,
                          eval(Filed.text)))), lambda Filed: setattr(Filed, "text",
                                                                     str(Filed.Obj.rotation_z)),
                             lambda Filed: str(getattr(Filed.Obj.rotation, "z")),
                             "1234567890.-", False),

            "Scale x: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "scale_x", eval(Filed.text))),
                          lambda Field: setattr(Field, "text",
                                                str(Field.Obj.scale_x)),
                          lambda Filed: str(getattr(Filed.Obj.scale, "x")),
                          "1234567890.-", False),
            "Scale y: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "scale_y", eval(Filed.text))),
                          lambda Filed: setattr(Filed, "text",
                                                str(Filed.Obj.scale_y)),
                          lambda Filed: str(getattr(Filed.Obj.scale, "y")),
                          "1234567890.-", False),
            "Scale z: ": (lambda Filed: MultiFunctionCaller(
                Func(setattr, Filed.Obj, "scale_z", eval(Filed.text))),
                          lambda Filed: setattr(Filed, "text",
                                                str(Filed.Obj.scale.z)),
                          lambda Filed: str(getattr(Filed.Obj.scale, "z")),
                          "1234567890.-", False)}

        self.UniversalParentEntity = Entity(parent=camera.ui, enabled=True)
        self.ObjetInformationParentEntity = Entity(parent=self.UniversalParentEntity, scale=(55 / 90, window.size.y),
                                                   model=Quad(aspect=3, radius=0), color=color.tint(color.gray, -.1),
                                                   position=window.right)
        self.TimelineParentEntity = Entity(parent=camera.ui, scale=(window.size.x, 50 / 90),
                                           model=Quad(aspect=3, radius=0), color=color.gray,
                                           position=window.bottom)

        self.WorldGrid = [
            Entity(parent=self, model=Grid(200, 200, thickness=2), rotation_x=90, scale=Vec3(200, 200, 200),
                   collider=None,
                   color=color.red),
            Entity(parent=self, model=Grid(100, 100, thickness=3), rotation_x=90, scale=Vec3(200, 200, 200),
                   collider=None,
                   color=color.black33),
            Entity(parent=self, model=Grid(400, 400), rotation_x=90, scale=Vec3(40, 40, 40), collider=None,
                   color=color.green)]

        self.DirectionEntity = DirectionBox(parent=camera.ui, camera=self.EditorCamera, enabled=True,
                                            always_on_top=True, render_queue=1)

    def AddEntityInScene(self):
        self.WorldItems.append(
            Entity(name=f"item_{len(self.WorldItems)}", parent=scene, model="cube", texture="white_cube",
                   collider="mesh", collision=True, color=color.white))
        self.ShowObjectContent(self.WorldItems[-1], self.SideBarTopSlideHandler)
        self.ToEditEntity = self.WorldItems[-1]
        self.AddGizmoTo(self.WorldItems[-1])

    def ShowObjectContent(self, Obj, Parent: Entity):
        self.TempLen = len(Parent.children)
        for i in range(self.TempLen - 1, -1, -1):
            destroy(Parent.children[i])
        del self.TempLen
        Parent.children = []

        Text(parent=Parent, text=type(Obj).__name__, scale=3, origin=(0, 0), y=.45, z=20, scale_x=3.5)
        Entity(name="Line", parent=Parent, model="line", color=color.black, scale=Vec3(0.99, 1.02, 1),
               position=Vec3(0.01, 0.39, 20))

        for i in range(len(self.BasicFunctions)):
            Text(parent=Parent, text=f"{self.BasicFunctions[i]}", scale=2, y=-i * 0.08 + .36, z=20, x=-.47)

        for i in range(len(self.BasicFunctions)):
            if self.BasicFunctions[i] in self.SpecialFunctions.keys():
                self.SpecialFunctions[self.BasicFunctions[i]](Obj, Parent, i)
            else:
                def UpdateFieldContent(field):
                    if field.active:
                        return

                    if type(getattr(field.Obj, field.name)) in (int, float) and not self.IsFieldActive:
                        # if getattr(Obj,field.name) == field.text:
                        field.text = f"{round(getattr(field.Obj, field.name), 11)}"

                TempChild = InputField(submit_on=["enter", "escape"], parent=Parent, y=-i * 0.08 + .34, z=-20, x=.13,
                                       active=False, text_scale=.75, cursor_y=.1, enter_active=True, character_limit=13,
                                       Obj=Obj)

                if self.BasicFunctions[i] in self.SpecialExtractingMethods.keys():
                    TempChild.SetNewValue = self.SpecialExtractingMethods[self.BasicFunctions[i]][0]
                    TempChild.DumpValue = self.SpecialExtractingMethods[self.BasicFunctions[i]][2]
                    TempChild.limit_content_to = self.SpecialExtractingMethods[self.BasicFunctions[i]][3]
                    TempChild.text = f"{TempChild.DumpValue(TempChild)}"
                    TempChild.on_submit = Func(TempChild.SetNewValue, TempChild)
                    if self.SpecialExtractingMethods[self.BasicFunctions[i]][4]:

                        TempChild.ToUpdateOnEnter = Func(MultiFunctionCaller,
                                                         Func(self.SpecialExtractingMethods[self.BasicFunctions[i]][1],
                                                              TempChild), Func(self.UpdateItemContent, Obj, Parent))

                    else:
                        TempChild.UpdateContent = self.SpecialExtractingMethods[self.BasicFunctions[i]][1]

                else:
                    def TryExtractData(Field):
                        return float(Field.text)

                    TempChild.text = f"{getattr(Obj, TextToVar(self.BasicFunctions[i], '_'))}"
                    TempChild.ExtractData = TryExtractData
                    TempChild.name = TextToVar(self.BasicFunctions[i], '_')

                    def ReturnName(field):
                        return setattr(field.Obj, f"{field.name}", eval(field.text))

                    TempChild.SetNewValue = ReturnName

                    TempChild.UpdateContent = UpdateFieldContent
                    TempChild.on_submit = Func(self.UpdateItemContent, Obj, Parent)

    def update(self):
        if 1 < distance(camera.position, (0, 0, 0)):
            self.distance = distance(camera.position, (0, 0, 0))
            if self.distance > 150:
                self.distance = 150
        else:
            self.distance = 0

        if self.distance > 10:
            self.WorldGrid[0].color = color.rgba(70, 70, 70, 1000 / self.distance)
            if int(self.WorldGrid[0].color[3]) == 0 and self.distance < 50: self.WorldGrid[0].enable()

            self.WorldGrid[1].color = color.rgba(50, 50, 50, self.distance)
            if int(self.WorldGrid[1].color[3]) == 0: self.WorldGrid[1].enable()

            self.WorldGrid[2].color = color.rgba(0, 0, 0, 200 / self.distance)
            if int(self.WorldGrid[2].color[3]) == 0 and self.distance < 50: self.WorldGrid[2].enable()

        if self.distance < 10:
            self.WorldGrid[1].color = color.rgba(50, 50, 50, 0)
            self.WorldGrid[1].disable()

        if self.distance > 50:
            self.WorldGrid[2].color = color.rgba(0, 0, 0, 0)
            self.WorldGrid[2].disable()
            self.WorldGrid[0].color = (70, 70, 70, 0)
            self.WorldGrid[0].disable()



