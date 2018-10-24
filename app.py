from flask import Flask, render_template, request, jsonify, send_from_directory

import logging
log = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/todo"

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
