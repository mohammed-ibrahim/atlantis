from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


"""
create table tasks (
    id int(11) NOT NULL AUTO_INCREMENT,
    detail TEXT default null,
    ref varchar(100) default null,
    position int(11) default null,
    created_at datetime default null,
    modified_at datetime default null,
    primary key(id)
)
"""

def _get_date():
    return datetime.datetime.now()

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column('id', db.Integer, primary_key=True)
    detail = db.Column('detail', db.String)
    ref = db.Column('ref', db.String)
    created_at = db.Column('created_at', db.Date)
    modified_at = db.Column('modified_at', db.Date, onupdate=_get_date)

    def __repr__(self):
        return "<Task(id='%s', title='%s', ref='%s')>" % (self.id, self.title, self.ref)
