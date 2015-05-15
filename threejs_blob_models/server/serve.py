import tornado.ioloop
import tornado.web
import numpy
import os
from threejs_blob_models.server.geometry import construct_cube

class ModelTypesHandler(tornado.web.RequestHandler):
    def initialize(self, model_types):
        self.model_types = model_types

    def get(self):
        self.write({'model_types': self.model_types})

class ModelHandler(tornado.web.RequestHandler):
    def initialize(self, blobs):
        self.blobs = blobs

    def get(self, model_type):
        blob = self.blobs.get(model_type, None)

        if blob is not None:
            print('Writing: {}'.format(blob))
            self.write(blob)
        else:
            raise tornado.web.HTTPError(404)


blobs = {'Cube': construct_cube().tostring()}

application = tornado.web.Application([
    (r'/model/(.*)', ModelHandler, {'blobs': blobs}),
    (r'/model-types', ModelTypesHandler, {'model_types': sorted(list(blobs.keys()))}),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': os.path.abspath(os.path.join(__file__, '..', '..', 'client')),
                                               'default_filename': 'index.html'}),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()