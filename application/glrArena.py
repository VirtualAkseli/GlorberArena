from flask import render_template
from application import app

  
posts = ["Tämä on varsin harmillista", "Sienestämisen underground-skene", "Kallioluolan mysteeri; kirkko vai katakombi?"]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def content():
	return render_template("posts.html", posts=posts)


