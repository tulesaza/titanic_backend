import tornado.web
import pandas as pd
import io
import numpy as np


class UploadHandler(tornado.web.RequestHandler):
    def initialize(self, shared_dict):
        self.shared_dict = shared_dict

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def post(self):
        fileinfo = self.request.files['filearg'][0]
        df = pd.read_csv(io.BytesIO(fileinfo['body']), encoding='utf8', sep=",", dtype={"switch": np.int8})
        self.shared_dict['df'] = df
        print(df.head())
        self.finish("File is uploaded!")