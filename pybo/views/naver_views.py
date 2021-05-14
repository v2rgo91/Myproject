from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.naver_api import naverbook
from ..forms import NaverBookForm

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book/', methods=('GET','POST'))
def Naverbook():
    form = NaverBookForm()

    if request.method == "POST" and form.validate_on_submit():
        result = naverbook(form.search.data)
        return render_template('naver/naverbook.html', bookinfo_list=result['items'],form=form)

    return render_template('naver/naverbook.html',form=form)

