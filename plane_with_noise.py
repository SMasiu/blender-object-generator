# import bpy
import random

vertices = []
faces = []

plane_size = 20
plane_fraction_size = 5
noise_size = 10

faces_iter = 0

for i in range(0, plane_size + 1):
    for j in range(0, plane_size + 1):
        vertices.append((plane_fraction_size * j, i * plane_fraction_size, random.randrange(0, noise_size)))

        if i != plane_size:
            if j != plane_size:
                faces.append((faces_iter, faces_iter + plane_size + 1, faces_iter + plane_size + 2))
                faces.append((faces_iter + plane_size + 2, faces_iter + 1, faces_iter))

            faces_iter += 1

print(vertices)
print(faces)

my_mesh = bpy.data.meshes.new("Cube")
my_object = bpy.data.objects.new("Cube", my_mesh)

my_object.location = (0, 0, 0)

bpy.context.scene.collection.objects.link(my_object)

my_mesh.from_pydata(vertices, [], faces)
my_mesh.update(calc_edges=True)

my_object.modifiers.new(name='subsurf', type='SUBSURF')

my_object.modifiers.get('subsurf').levels = 2

for poly in my_object.data.polygons:
    poly.use_smooth = True