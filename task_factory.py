
from model import Task
import uuid


def build_task(params):
    if 'title' not in params or params['title'].strip() == '':
        return (False, None, "Title is invalid")

    reference_id = str(uuid.uuid4())
    task = Task(title = params['title'], ref = reference_id)

    return (True, task, None)

def to_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
