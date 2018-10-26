from flask import Flask, render_template, request, jsonify, send_from_directory

import logging
log = logging.getLogger(__name__)

from flask.json import JSONEncoder
from datetime import date

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/todo"
app.json_encoder = CustomJSONEncoder


from views import *

def setup_defaults():
    log_formatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # logger_file_name = "cerebro-scraper.output.log"
    # logger_file_full_path = os.path.join("./", logger_file_name)
    # file_handler = logging.FileHandler(logger_file_full_path)
    # file_handler.setFormatter(log_formatter)
    # root_logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

if __name__ == '__main__':
    setup_defaults()
    app.run(port = 7272, debug = True)
    # app.run(port = 7272)
