import tornado.web
from metrics.metrics import calculate_roc_curve


class MetricsViewHandler(tornado.web.RequestHandler):

    def initialize(self, shared_dict):
        self.shared_dict = shared_dict

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def get(self):
        X, y = self.shared_dict['X_test'], self.shared_dict["y_test"]
        log_reg = self.shared_dict['log_reg']
        scores = log_reg.predict_proba(X)
        results = calculate_roc_curve(y, scores)
        self.finish(results)