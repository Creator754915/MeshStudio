from ursina import *
from ObjectOriented.Gizmo.PositionGizmo import PositionGizmo
from ObjectOriented.Gizmo.ScaleGizmo import ScaleGizmo


class AddEntity(Entity):
    def __init__(self, parent=scene, model="cube", name="Entity1", color=color.black66, scale=(1, 1, 1)):
        super().__init__(parent=parent, model=model, color=color, name=name, scale=scale)

        self.positionGizmo = PositionGizmo(self, 0, lambda: ...)
        self.scaleGizmo = ScaleGizmo(self, lambda: ...)

        self.positionGizmo.SetUp()
        self.scaleGizmo.SetUp()

        self.positionGizmo.enabled = True
        self.scaleGizmo.enabled = False

        self.EntityName = Button(parent=self, model=None, text=name, position=(0, self.scale.y * 2, 0), scale=0.6)

        self.globalInformation = f'''
Global Information
    -Entity name: {self.name}
    -Entity Position: {self.position}
    -Entity Rotation: {self.rotation}
    -Entity Scale: {self.scale}'''

        # self.TEXT = Text(text=self.globalInformation, align="left")

    # def update(self):
    #     self.globalInformation = f'''
    #     Global Information
    #         -Entity name: {self.name}
    #         -Entity Position: {self.position}
    #         -Entity Rotation: {self.rotation}
    #         -Entity Scale: {self.scale}'''
    #     self.TEXT.text = self.globalInformation

    def PositionGizmoEnabled(self, Enable: bool):
        if Enable:
            self.positionGizmo.enabled = Enable
            self.scaleGizmo.enabled = False
        else:
            self.positionGizmo.enabled = Enable
            self.scaleGizmo.enabled = True

    def ScaleGizmoEnabled(self, Enable: bool):
        if Enable:
            self.scaleGizmo.enabled = Enable
            self.positionGizmo.enabled = False
        else:
            self.scaleGizmo.enabled = Enable
            self.positionGizmo.enabled = True

    def DestroyGizmo(self):
        destroy(self.positionGizmo, self.scaleGizmo)


if __name__ == "__main__":
    app = Ursina()

    EditorCamera()

    cube = AddEntity()

    app.run()
