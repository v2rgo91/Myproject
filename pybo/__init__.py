from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
# from pybo.views import question_views

db=SQLAlchemy()             # 코드 위치 및 순서 중요
migrate = Migrate()          # 코드 위치 및 순서 중요


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models     # 코드 위치 중요

    from .views import main_views, question_views, answer_views, naver_views, movie_views, auth_views, movie_search_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(naver_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(movie_views.bp)
    app.register_blueprint(movie_search_views.bp)

    # from .filters import format_str
    # app.jinja_env.filters['string'] = format_str

    return app




