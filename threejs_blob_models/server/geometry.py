import numpy

def construct_cube():
    bottom = numpy.array([-1, -1, -1, 1, -1, -1,
                          1, -1, -1, 1, -1, 1,
                          1, -1, 1, -1, -1, 1,
                          -1, -1, 1, -1, -1, -1], dtype=numpy.float32)

    top = numpy.copy(bottom)
    top[1::3] = 1

    bottom_vertices = bottom.reshape(4, -1)[:, :3]
    top_verices = numpy.copy(bottom_vertices)
    top_verices[:, 1] = 1
    side_vertices = numpy.hstack((bottom_vertices, top_verices)).flatten()

    concatenated = numpy.hstack((bottom, top, side_vertices))

    return concatenated