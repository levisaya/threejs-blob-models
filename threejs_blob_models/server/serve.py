import tornado.ioloop
import tornado.web
import numpy
import os
from threejs_blob_models.server.geometry import construct_cube, construct_pyramid, construct_noisecube

class ModelTypesHandler(tornado.web.RequestHandler):
    """
    Serve up the list of geometry types that are available.
    """
    def initialize(self, model_types):
        self.model_types = model_types

    def get(self):
        self.write({'model_types': self.model_types})

class ModelHandler(tornado.web.RequestHandler):
    """
    Serve the geometry binary blobs.
    """
    def initialize(self, blobs):
        self.blobs = blobs

    def get(self, model_type):
        blob = self.blobs.get(model_type, None)

        if blob is not None:
            self.write(blob)
        else:
            raise tornado.web.HTTPError(404)

if __name__ == "__main__":
    blobs = {'Cube': construct_cube().tostring(),
             'Pyramid': construct_pyramid().tostring(),
             'Noise Cube (1000 Lines)': construct_noisecube(1000).tostring(),
             'Noise Cube (1M Lines)': construct_noisecube(1000000).tostring()}

    application = tornado.web.Application([
        (r'/model/(.*)', ModelHandler, {'blobs': blobs}),
        (r'/model-types', ModelTypesHandler, {'model_types': sorted(list(blobs.keys()))}),
        (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.abspath(os.path.join(__file__, '..', '..', 'client')),
                                                   'default_filename': 'index.html'}),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()