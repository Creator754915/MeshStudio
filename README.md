<p align="center">
  <img src="meshstudio_logo.png">
  <br>
  <img src="https://img.shields.io/badge/Version-1.5.0.0-green?style=for-the-badge">
  <br>
  <img src="https://img.shields.io/badge/Author-Creator754915-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-lightblue?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FCreator754915%2FMeshStudio&title=Visitors&edge_flat=false"/></a>
</p>

# MeshStudio
MeshStudio is a 3d software, texture editor and sound creator.

MeshStudio is a software created entirely with the Python and with Ursina Engine library.

This software has several external features and plugins created by the community

### **WARNING!** 

**YOU NEED INSTALL ```pip install https://github.com/Creator754915/Ursina.More.UI.git```**

# Features

<h2>General UI</h2>

![Main UI](https://github.com/Creator754915/MeshStudio/assets/106489587/594d9224-5d48-42aa-aea6-8b295c743d05)


<h2>Lights</h2>

<img src="Features/lights.png">

<h2>Physics</h2>

<img src="Features/physics.png">

<h2>Modelisation</h2>

![model](https://github.com/Creator754915/MeshStudio/assets/106489587/47d05ec8-ba7e-45b2-ae47-f624e8691627)

<h2>Timeline</h2>

![Timeline](https://github.com/Creator754915/MeshStudio/assets/106489587/88f59e51-8996-432a-a636-745f3b45d85c)

**Animation Example:**

```json
{
   "frame": {
      "0": {
         "model": {
            "name": "HELLO",
            "position": [
               0.0,
               0.0,
               0.0
            ],
            "scale": [
               1.0,
               1.0,
               1.0
            ],
            "color": "Color(1.0, 1.0, 1.0, 1.0)"
         }
      },
      "36": {
         "model": {
            "name": "HELLO",
            "position": [
               -3.188293933868408,
               0.08317279070615768,
               2.682209014892578e-07
            ],
            "scale": [
               1.0,
               1.0,
               1.0
            ],
            "color": "Color(1.0, 1.0, 1.0, 1.0)"
         }
      }
   }
}
```

<br>

<h2>Texture Editor</h2>

![Texture Editor](https://github.com/Creator754915/MeshStudio/assets/106489587/82d9cae4-7b41-4da3-8009-9d6dc23063e8)

<p>Coming soon...</p>

<br>

# GeometryNodeEditor

![image](https://github.com/Creator754915/MeshStudio/assets/106489587/ef4122e5-5047-4ae9-8385-a52e6e2ce00a)

```
ColorNode(
    color = (255, 255, 255)
    size = (1, 1, 1)
    position = (0.5, 0, 0)
)
    
ModelNode(
    model="cube",
    scale=5
    position=(0, 0, 0)
)

CameraNode(
    camera=1,
    position=(-0.5, 0, 0)
)


INIT:
    ColorNode()
    ModelNode()
    CameraNode()
```

**Save model for GeometryNodeEditor**


## Keybinds:

  **shift + a**: Add an object

  **shift + r**: Rotate object
  
  **shift + t**: Modify the texture path
  
  **shift + s**: Save project
  
  **shift + o**: Open project

  **ctrl + right click**: Open Panel

  **left arrow / right arrow**: rotate object in the Y axis

  **up arrow / down arrow**: rotate object in the X axis

  **ctrl + scroll up**: + size to texture brush
  
  **ctrl + scroll down**: - size to texture brush

## Updates

### Patch 2.0.0
**New features**:
  1. RigidBody add

### Patch 1.1.0

**New features**:
   1. Rotate cube with new **gizmos**
   2. New **gizmos** for the **position** and for the **rotation**
   3. New **timeline system** with Panel

**Patch**:
   1. **Crash** when you try to **import object**


### Patch 1.0.0

**New features**:
   1. Rotate cube with the **arrows**
   2. Export model **OBJ** and **GLTF**
   3. Show **vertices** of cubes 

**Patch**:
   1. Fixed **multiple panel** open

## Examples

## The All Contributors Table

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a><img src="https://avatars.githubusercontent.com/u/121798131?v=4" width="100px;" alt="IndividualCoder"/><br /><sub><b>IndividualCoder</b></sub></a><br /><a href="https://github.com/IndividualCoder" title="Developper">💻</a> <a href="#talk-kentcdodds" title="Talks">📢</a></td>
    </tr>
  </tbody>
</table>


*Version BETA-1.5.0*
