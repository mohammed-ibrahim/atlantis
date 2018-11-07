
from model import Task
import datetime
import time
import format
import uuid

def get_due_date(params):
    due_date_field = 'due_date'
    if due_date_field not in params:
        return None

    formatted_date = params[due_date_field]
    if 'year' not in formatted_date or 'month' not in formatted_date or 'day' not in formatted_date:
        return None

    formatted_date = "%d-%d-%d" % (formatted_date['year'], formatted_date['month'], formatted_date['day'])
    parsed_date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")
    return parsed_date


def build_task(params):
    detail_field = 'title'
    if detail_field not in params or params[detail_field].strip() == '':
        return (False, None, "Title is invalid")

    reference_id = str(uuid.uuid4())
    task = Task(title = params[detail_field], ref = reference_id, created_at = datetime.datetime.now(), modified_at = datetime.datetime.now())

    due_date = get_due_date(params)
    if due_date:
        task.due_date = due_date

    task.status = "ACTIVE"

    return (True, task, None)

def compute_hr_diff(days):
    if days == 0:
        return "Today"

    if days == 1:
        return "Yesterday"

    return str(days) + " days back."

def to_raw(row):
    d = {}
    for column in row.__table__.columns:
        col_name = column.name
        data_obj = getattr(row, col_name)
        d[col_name] = str(data_obj)

        if isinstance(data_obj, datetime.date):
            diff_days = (datetime.datetime.now() - data_obj).days
            d[col_name + "_cf"] = {
                "diff" : diff_days,
                "year": data_obj.year,
                "month": data_obj.month,
                "day": data_obj.day,
                "month_txt": data_obj.strftime("%B"),
                "hr_diff": compute_hr_diff(diff_days)
            }

    return d

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
