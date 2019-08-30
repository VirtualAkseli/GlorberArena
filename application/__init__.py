from flask import Flask
app = Flask(__name__)


from application import glrArena
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.posts import models
from application.posts import views
from application.authentication import models 
from application.authentication import views 

from application.authentication.models import User

from application.profiles import views 
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Log in to access all features."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass
