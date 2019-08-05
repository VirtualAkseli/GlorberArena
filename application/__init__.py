from flask import Flask
app = Flask(__name__)

from application import glrArena 

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
from application import glrArena
from application.posts import models
from application.posts import views
db.create_all()
