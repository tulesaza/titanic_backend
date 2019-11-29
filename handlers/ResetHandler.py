import tornado.web


class ResetHandler(tornado.web.RequestHandler):

    def initialize(self, shared_dict):
        self.shared_dict = shared_dict

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def post(self):
        self.shared_dict.clear()
        self.write("Cleaned up")