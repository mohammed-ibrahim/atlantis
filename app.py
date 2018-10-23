from flask import Flask, render_template, request, jsonify, send_from_directory


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/todo"

from views import *

if __name__ == '__main__':
    app.run(port = 7272, debug = True)
