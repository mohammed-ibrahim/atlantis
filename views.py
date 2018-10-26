from flask import render_template, request, redirect, flash, url_for, abort, send_from_directory, jsonify
from model import Task, db
from app import app
import task_factory
import json
import sqlalchemy

import logging
log = logging.getLogger(__name__)


#    _____         .__
#   /  _  \ ______ |__|
#  /  /_\  \\____ \|  |
# /    |    \  |_> >  |
# \____|__  /   __/|__|
#         \/|__|

@app.route('/api/new', methods=['POST'])
def new_task():

    if not request.json:
        abort(400)

    # log.info(request.text)
    data = request.json
    (status, task, message) = task_factory.build_task(data)

    if status:
        try:
            db.session.add(task)
            db.session.commit()
            log.info("Succesfully added %s", task.ref)
            return task.ref
        except Exception, e:
            log.error("Failed %s", str(e))

    return "Failed", 500


@app.route('/api/tasks', methods=['GET'])
def get_task():
    tasks = Task.query.filter(Task.status == 'ACTIVE').order_by(sqlalchemy.asc(Task.modified_at)).all()
    content = []
    for task in tasks:
        content.append(task_factory.to_raw(task))
        # print(json.dumps(task_factory.to_raw(task)))

    return json.dumps(content)

#   ___ ___   __          .__
#  /   |   \_/  |_  _____ |  |
# /    ~    \   __\/     \|  |
# \    Y    /|  | |  Y Y  \  |__
#  \___|_  / |__| |__|_|  /____/
#        \/             \/
@app.route('/')
def home_page():
    # tasks = Task.query.filter(Task.status == 'ACTIVE').order_by(sqlalchemy.asc(Task.modified_at)).all()

    # content = []
    # for task in tasks:
    #     content.append(task_factory.to_dict(task))

    # return render_template('index.html', page_data = content)
    return send_from_directory('templates', 'index.html')

# @app.route('/new')
# def new_task_html():
#     return render_template('new-task.html')
