from pybo import db
from datetime import datetime

class User_info(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    pw = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    addr = db.Column(db.String(3), nullable=False)
    birth = db.Column(db.String(6),  nullable=False)
    sex = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.String(6), nullable=False)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


 # default=datetime.utcnow





