from flask import Blueprint, render_template, url_for, request
from werkzeug.utils import redirect
from pybo.movie_search_api import moviesearch
from ..forms import MovieSearchForm

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/movie/', methods=('GET','POST'))
def MovieSearch():
    form = MovieSearchForm()

    if request.method == "POST" and form.validate_on_submit():
        result = moviesearch(form.search.data)
        print(result)
        return render_template('movie/movieSearch.html', movie_list=result['items'],form=form)

    return render_template('movie/movieSearch.html',form=form)






