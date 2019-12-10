# import os
# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_mail import Message, Mail

# db = SQLAlchemy()
# login = LoginManager()

# def create_app(debug=False, test_config=None):
# 	app = Flask(__name__)
# 	app.debug = debug
# 	app.config.from_object(Config)

# 	if test_config is None:
# 		app.config.from_object('config.Config')
# 	else:
# 		app.config.from_mapping('config.Config')	

# 	db.init_app(app)
# 	login.init_app(app)
# 	login.login_view = 'login'	

# 	with app.app_context():
# 		 from . import routes, models
# 		 db.create_all()
		 
#     return app


# # app = Flask(__name__)
# # app.config.from_object(Config)


# # bcrypt = Bcrypt(app)

# # db = SQLAlchemy(app)

# # login = LoginManager(app)

# # login.login_view = 'login'

# # from app import routes, models
# ----------------
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(test_config=None):

    app = Flask(__name__)

    if test_config is None:
        #app.config.from_pyfile('config.py', silent=True)
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config.from_mapping(
            SECRET_KEY='dev',
            SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
            SQLALCHEMY_TRACK_MODIFICATIONS = False
        )
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # here are all the pieces of my program
    with app.app_context():
        from . import routes
        db.create_all()

    return app

