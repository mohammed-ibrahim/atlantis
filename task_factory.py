
from model import Task
import datetime
import format
import uuid



def build_task(params):
    detail_field = 'detail'
    if detail_field not in params or params[detail_field].strip() == '':
        return (False, None, "Title is invalid")

    reference_id = str(uuid.uuid4())
    task = Task(detail = params[detail_field], ref = reference_id, created_at = datetime.datetime.now(), modified_at = datetime.datetime.now())

    return (True, task, None)

def to_dict(row):
    d = {}
    for column in row.__table__.columns:
        if column.name == 'detail':
            d[column.name] = format.html_format(str(getattr(row, column.name)))
        else:
            d[column.name] = str(getattr(row, column.name))

    return d
