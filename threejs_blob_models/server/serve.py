import tornado.ioloop
import tornado.web
import numpy
import os

class GeometryTypesHandler(tornado.web.RequestHandler):
    def initialize(self, geometry_types):
        self.geometry_types = geometry_types

    def get(self):
        self.write({'geometry_types': self.geometry_types})

class GeometryHandler(tornado.web.RequestHandler):
    def initialize(self, blobs):
        self.blobs = blobs

    def get(self, geometry_type):
        blob = self.blobs.get(geometry_type, None)

        if blob is not None:
            self.write(blob)
        else:
            raise tornado.web.HTTPError(404)

cube = numpy.array([0, 0, 0, 1, 0, 0,
                    1, 0, 0, 1, 0, -1,
                    1, 0, -1, 0, 0, -1,
                    0, 0, -1, 0, 0, 0,
                    0, 1, 0, 1, 1, 0,
                    1, 1, 0, 1, 1, -1,
                    1, 1, -1, 0, 1, -1,
                    0, 1, -1, 0, 1, 0,
                    0, 0, 0, 0, 1, 0,
                    1, 0, 0, 1, 1, 0,
                    0, 0, -1, 0, 1, -1,
                    1, 0, -1, 1, 1, -1])
blobs = {'Cube': cube.tostring()}

application = tornado.web.Application([
    (r'/geometry/(.*)', GeometryHandler, {'blobs': blobs}),
    (r'/geometry-types', GeometryTypesHandler, {'geometry_types': sorted(list(blobs.keys()))}),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.abspath(os.path.join(__file__, '..', '..', 'client')),
                                               'default_filename': 'index.html'}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()