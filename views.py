from flask import render_template, request, redirect, flash,url_for
from model import Task
from app import app


@app.route('/')
def list_all():
    tasks = Task.query.all()

    titles = []
    for task in tasks:
        titles.append(task.title)

    return str(titles)
