from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


"""
create table tasks (
    id int(11) NOT NULL AUTO_INCREMENT,
    title varchar(1000) default null,
    ref varchar(100) default null,
    position int(11) default null,
    link_1 TEXT default null,
    link_2 TEXT default null,
    link_3 TEXT default null,
    description TEXT default null,
    created_at datetime default null,
    modified_at datetime default null,
    primary key(id)
)
"""

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    ref = db.Column('ref', db.String)
    link_1 = db.Column('link_1', db.String)
    link_2 = db.Column('link_2', db.String)
    link_3 = db.Column('link_3', db.String)
    description = db.Column('description', db.String)
    created_at = db.Column('created_at', db.Date)
    modified_at = db.Column('modified_at', db.Date)

    def __repr__(self):
        return "<Task(id='%s', title='%s', ref='%s')>" % (self.id, self.title, self.ref)
