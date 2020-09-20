import bpy
import math

cuts = 3
radius = 5
height = 10.0

vertices = []
faces = []

angle = 360.0 / cuts
current_angle = 0

bottom_vertices = []
top_vertices = []

bottom_face = ()
top_face = ()

for x in range(0, cuts):
    bottom_vertices.append((
        radius * math.sin(math.radians(current_angle)),
        radius * math.cos(math.radians(current_angle)),
        0.0
    ))
    top_vertices.append((
        radius * math.sin(math.radians(current_angle)),
        radius * math.cos(math.radians(current_angle)),
        height
    ))

    current_angle += angle

    bottom_face += (x,)
    top_face += (x + cuts,)

    if x < cuts - 1:
        faces.append((x, x + 1, x + 1 + cuts, x + cuts))

faces.append((0, cuts - 1, 2 * cuts - 1, cuts))
faces.append(bottom_face)
faces.append(top_face)

vertices += bottom_vertices + top_vertices

my_mesh = bpy.data.meshes.new("Cube")
my_object = bpy.data.objects.new("Cube", my_mesh)

my_object.location = (0, 0, 0)

bpy.context.scene.collection.objects.link(my_object)

my_mesh.from_pydata(vertices, [], faces)
my_mesh.update(calc_edges=True)
