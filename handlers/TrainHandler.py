import tornado.web
from preprocess.preproces_data import split_train_data, prepare_x_and_y
from ml_models.LogisticRegression import LogisticRegression

class TrainHandler(tornado.web.RequestHandler):

    def initialize(self, shared_dict):
        self.shared_dict = shared_dict

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def post(self):
        train, test = split_train_data(self.shared_dict['df'])
        X_train, y_train = prepare_x_and_y(train)
        self.shared_dict['X_test'], self.shared_dict["y_test"] = prepare_x_and_y(test)
        log_reg = LogisticRegression()
        log_reg.fit(X_train, y_train)
        self.shared_dict['log_reg'] = log_reg
        self.write("Model trained")
