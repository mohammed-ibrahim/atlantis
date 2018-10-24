
from model import Task
import datetime
import format
import uuid

def get_due_date(params):
    due_date_field = 'due_date'
    if due_date_field not in params or params[due_date_field].strip() == '':
        return None

    parsed_date = datetime.datetime.strptime(params[due_date_field], "%Y-%m-%d")
    return parsed_date


def build_task(params):
    detail_field = 'detail'
    if detail_field not in params or params[detail_field].strip() == '':
        return (False, None, "Title is invalid")

    reference_id = str(uuid.uuid4())
    task = Task(detail = params[detail_field], ref = reference_id, created_at = datetime.datetime.now(), modified_at = datetime.datetime.now())

    due_date = get_due_date(params)
    if due_date:
        task.due_date = due_date

    return (True, task, None)

def to_dict(row):
    d = {}
    # for column in row.__table__.columns:
    #     if column.name == 'detail':
    #         d[column.name] = format.html_format(str(getattr(row, column.name)))
    #     else:
    #         d[column.name] = str(getattr(row, column.name))

    # d['detail']
    d['ref'] = row.ref
    d['id'] = row.id
    parsed = format.parse(row.detail)
    d['title'] = parsed['title']
    d['content'] = parsed['content']
    d['meta'] = parsed['meta']

    return d
