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
            return json.dumps({'ref_id': task.ref})
        except Exception, e:
            log.error("Failed %s", str(e))

    return "Failed", 500


@app.route('/api/tasks', methods=['GET'])
def get_task():
    tasks = Task.query.filter(Task.status == 'ACTIVE').order_by(sqlalchemy.desc(Task.modified_at)).all()
    content = []
    for task in tasks:
        content.append(task_factory.to_raw(task))
        # print(json.dumps(task_factory.to_raw(task)))

    return jsonify({'tasks': content})

@app.route('/api/task/<task_ref>', methods=['GET'])
def get_task_by_ref(task_ref):
    task = Task.query.filter(Task.ref == task_ref).first()
    return jsonify(task_factory.to_raw(task))

#   ___ ___   __          .__
#  /   |   \_/  |_  _____ |  |
# /    ~    \   __\/     \|  |
# \    Y    /|  | |  Y Y  \  |__
#  \___|_  / |__| |__|_|  /____/
#        \/             \/
@app.route('/')
def fresh_home_page():
    # tasks = Task.query.filter(Task.status == 'ACTIVE').order_by(sqlalchemy.asc(Task.modified_at)).all()

    # content = []
    # for task in tasks:
    #     content.append(task_factory.to_dict(task))

    # return render_template('index.html', page_data = content)
    return send_from_directory('templates', 'index.html')

@app.route('/angular')
def new_home_angular():
    # tasks = Task.query.filter(Task.status == 'ACTIVE').order_by(sqlalchemy.asc(Task.modified_at)).all()

    # content = []
    # for task in tasks:
    #     content.append(task_factory.to_dict(task))

    # return render_template('index.html', page_data = content)
    return send_from_directory('templates', 'new-home.html')

# @app.route('/new')
# def new_task_html():
#     return render_template('new-task.html')
