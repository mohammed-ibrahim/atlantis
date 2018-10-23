from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


"""
create table tasks (
    id int(11) NOT NULL AUTO_INCREMENT,
    title varchar(1000) default null,
    ref varchar(100) default null,
    primary key(id)
)
"""

class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    ref = db.Column('ref', db.String)

    def __repr__(self):
        return "<Task(id='%s', title='%s', ref='%s')>" % (self.id, self.title, self.ref)

    def to_json(self):
        return {
            "ref": self.ref,
            "title": self.title
        }
