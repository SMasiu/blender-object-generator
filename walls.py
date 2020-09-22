import bpy


def add_mesh_scene(vertices, faces):
    my_mesh = bpy.data.meshes.new("Cube")
    my_object = bpy.data.objects.new("Cube", my_mesh)

    my_object.location = (0, 0, 0)

    bpy.context.scene.collection.objects.link(my_object)

    my_mesh.from_pydata(vertices, [], faces)
    my_mesh.update(calc_edges=True)


def main():
    wall_corners = [
        [(0.0, 0.0), (5.0, 0.0), (6.0, 0.0), (9.0, 0.0)],
        [(0.0, 2.0), (5.0, 2.0), (6.0, 2.0), (9.0, 2.0)],
        [(0.0, 6.0), (5.0, 6.0), (6.0, 6.0), (9.0, 6.0)]
    ]

    wall_height = 2.4

    vertices = []
    faces = []

    wall_thickness = 0.3
    faces_iter = 0

    y_offset = 0

    vertices_bottom = []
    vertices_top = []

    y_len = len(wall_corners)
    x_len = len(wall_corners[0])
    top_level_index = 4 * x_len * y_len
    y_iter = 0

    for corner_row in wall_corners:
        x_offset = 0
        x_iter = 0
        for corner in corner_row:
            (x, y) = corner
            x += x_offset
            y += y_offset

            vertices_bottom.append((x, y, 0.0))
            vertices_bottom.append((x, y + wall_thickness, 0.0))
            vertices_bottom.append((x + wall_thickness, y + wall_thickness, 0.0))
            vertices_bottom.append((x + wall_thickness, y, 0.0))

            vertices_top.append((x, y, wall_height))
            vertices_top.append((x, y + wall_thickness, wall_height))
            vertices_top.append((x + wall_thickness, y + wall_thickness, wall_height))
            vertices_top.append((x + wall_thickness, y, wall_height))

            faces.append((faces_iter, faces_iter + 1, faces_iter + 2, faces_iter + 3))
            faces.append((
                faces_iter + top_level_index,
                faces_iter + 1 + top_level_index,
                faces_iter + 2 + top_level_index,
                faces_iter + 3 + top_level_index
            ))

            if x_iter != x_len - 1:
                faces.append((faces_iter + 2, faces_iter + 3, faces_iter + 4, faces_iter + 5))
                faces.append((
                    faces_iter + top_level_index + 2,
                    faces_iter + top_level_index + 3,
                    faces_iter + top_level_index + 4,
                    faces_iter + top_level_index + 5
                ))

            if y_iter != y_len - 1:
                faces.append((
                    faces_iter + 1,
                    faces_iter + 2,
                    faces_iter + 4 * x_len + 3,
                    faces_iter + 4 * x_len
                ))
                print(faces_iter + 4 * x_len + top_level_index)
                faces.append((
                    faces_iter + top_level_index + 1,
                    faces_iter + top_level_index + 2,
                    faces_iter + 4 * x_len + 3 + top_level_index,
                    faces_iter + 4 * x_len + top_level_index
                ))

            faces_iter += 4
            x_offset += wall_thickness
            x_iter += 1
        y_offset += wall_thickness
        y_iter += 1

    vertices += vertices_bottom + vertices_top
    print(vertices)
    print(faces)

    add_mesh_scene(vertices, faces)


main()
