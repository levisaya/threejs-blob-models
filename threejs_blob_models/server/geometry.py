import numpy

def construct_cube():
    """
    Constructs a vertex buffer containing the line segments of a wireframe cube.
    Array is of the LinePieces style, so [vert1, vert2, vert3, vert4] means two lines, from 1 to 2 and 3 to 4.
    :return: numpy.array, dtype=float32, shape=(72)
    """

    # Line segments that show up on the bottom of the cube, y = -1.
    bottom = numpy.array([-1, -1, -1, 1, -1, -1,
                          1, -1, -1, 1, -1, 1,
                          1, -1, 1, -1, -1, 1,
                          -1, -1, 1, -1, -1, -1], dtype=numpy.float32)

    # Copy, change the y-coordinate to 1 to get the top.
    top = numpy.copy(bottom)
    top[1::3] = 1

    # Slice off the start points of each line to get the bottom vertices
    bottom_vertices = bottom.reshape(4, -1)[:, :3]

    # Change the y-coordinate to 1 to get the top vertices.
    top_verices = numpy.copy(bottom_vertices)
    top_verices[:, 1] = 1

    # Add lines from the bottom to top vertices.
    side_vertices = numpy.hstack((bottom_vertices, top_verices)).flatten()

    # Smash the bottom, top and sides into one vertex array.
    return numpy.hstack((bottom, top, side_vertices))

def construct_pyramid():
    """
    Constructs a vertex buffer containing the line segments of a wireframe pyramid.
    Array is of the LinePieces style, so [vert1, vert2, vert3, vert4] means two lines, from 1 to 2 and 3 to 4.
    :return: numpy.array, dtype=float32, shape=(48)
    """

    # Line segments that show up on the bottom of the pyramid, y = -1.
    bottom = numpy.array([-1, -1, -1, 1, -1, -1,
                          1, -1, -1, 1, -1, 1,
                          1, -1, 1, -1, -1, 1,
                          -1, -1, 1, -1, -1, -1], dtype=numpy.float32)

    # Slice off the start points of each line to get the bottom vertices
    bottom_vertices = bottom.reshape(4, -1)[:, :3]

    # Stack the top vertex to match with each bottom vertex.
    top_vertex = numpy.array([0, 1, 0], dtype=numpy.float32)
    top_vertices = numpy.vstack((top_vertex, top_vertex, top_vertex, top_vertex))

    # Stack so we get lines from each bottom vertex to the top.
    side_lines = numpy.hstack((bottom_vertices, top_vertices)).flatten()

    # Smash the bottom and sides into one vertex array.
    return numpy.hstack((bottom, side_lines))

def construct_noisecube(num_segments):
    """
    Constructs a vertex buffer containing the line segments of a noise cube.
    This consists of random line segments, with all vertex coordinates -1 <= coordinate <= 1
    Array is of the LinePieces style, so [vert1, vert2, vert3, vert4] means two lines, from 1 to 2 and 3 to 4.
    :param num_segments: The number of desired random line segments.
    :type num_segments: int
    :return: numpy.array, dtype=float32, shape=(num_segments * 6)
    """
    return numpy.random.uniform(low=-1.0, high=1.0, size=(num_segments * 6)).astype(numpy.float32)
