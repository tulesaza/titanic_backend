import tornado.ioloop
import tornado.web

from handlers.MetricsViewHandler import MetricsViewHandler
from handlers.ResetHandler import ResetHandler
from handlers.TrainHandler import TrainHandler
from handlers.UploadHandler import UploadHandler

session_storage = dict()


def make_app():
    return tornado.web.Application([
        (r"/train", TrainHandler, dict(shared_dict=session_storage)),
        (r"/upload", UploadHandler, dict(shared_dict=session_storage)),
        (r"/view", MetricsViewHandler, dict(shared_dict=session_storage)),
        (r"/reset", ResetHandler, dict(shared_dict=session_storage))
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()
