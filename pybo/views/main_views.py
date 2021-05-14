from flask import Blueprint, render_template, url_for
from pybo import db
from pybo.models import User_info, Question, Answer
import os
from datetime import datetime
from werkzeug.utils import import_string, redirect

# basdir = os.path.abspath(os.path.dirname(__file__))
# dbfile = os.path.join(basdir, 'db.sqlite')

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    q1 = User_info(id='abc', pw='ab123', name='가나다', age=20, addr='서울', birth='020101', sex='m', create_date='210101')
    q2 = User_info(id='def', pw='de456', name='마바사', age=21, addr='부산', birth='010101', sex='f', create_date='210102')
    q3 = User_info(id='ghi', pw='gh789', name='아자차', age=22, addr='대전', birth='000101', sex='m', create_date='210301')
    q4 = User_info(id='jkl', pw='jk321', name='카타파', age=23, addr='울산', birth='990101', sex='f', create_date='210403')
    q5 = User_info(id='mno', pw='mn654', name='하거너', age=24, addr='광주', birth='980101', sex='m', create_date='210203')
    q6 = User_info(id='pqr', pw='pq987', name='더러머', age=25, addr='제주', birth='970101', sex='f', create_date='210305')
    q7 = User_info(id='stu', pw='st135', name='버서어', age=26, addr='강원', birth='960101', sex='m', create_date='200203')
    q8 = User_info(id='vwx', pw='vw246', name='저처커', age=27, addr='청주', birth='950101', sex='f', create_date='190503')
    q9 = User_info(id='yza', pw='yz369', name='허고노', age=28, addr='대구', birth='940101', sex='m', create_date='210813')
    q10 = User_info(id='bcd', pw='bc012', name='도로모', age=29, addr='경기', birth='930101', sex='f', create_date='201224')

    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.add(q4)
    db.session.add(q5)
    db.session.add(q6)
    db.session.add(q7)
    db.session.add(q8)
    db.session.add(q9)
    db.session.add(q10)
    db.session.commit()
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/detail.html', question=question)




# @bp.route('/hello')
# def hello_pybo():
#     result = Question.query.filter(Question.id=1).all
#     result = Question.query.get(1)  #id(primary key)가 1번데이터를 가져옴
#     q = Question.query.get(2)
#     print(q)
#     # a = Answer(question = q, content='답변 3번', create_date=datetime.now())
#     # db.session.add(a)
#
#     db.session.commit()
#
#     return 'Hello, Pybo!'

