from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from sqlalchemy import Boolean, Integer, Column, ForeignKey, String

# Initializing an instance of the SQLAlchemy class
db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id


# db.create_all()
