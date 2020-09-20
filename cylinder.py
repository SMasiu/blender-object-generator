import bpy
import math

cuts = 3
radius = 5
height = 10.0

vertices = [(0.0, 0.0, 0.0), (0.0, 0.0, height)]
faces = []

angle = 360.0 / cuts


def append_circle_base(center_vertex_index: int, offset_face: int, z_axis: float):
    current_angle = 0
    for x in range(0, cuts + 1):
        vertices.append((
            radius * math.sin(math.radians(current_angle)),
            radius * math.cos(math.radians(current_angle)),
            z_axis
        ))
        current_angle += angle

        if x != cuts:
            faces.append((center_vertex_index, x + offset_face, x + 1 + offset_face))


append_circle_base(0, 2, 0)
append_circle_base(1, 3 + cuts, height)

print(vertices)
print(faces)

print(len(vertices))
print(len(faces))

my_mesh = bpy.data.meshes.new("Cube")
my_object = bpy.data.objects.new("Cube", my_mesh)

my_object.location = (0, 0, 0)

bpy.context.scene.collection.objects.link(my_object)

my_mesh.from_pydata(vertices, [], faces)
my_mesh.update(calc_edges=True)
