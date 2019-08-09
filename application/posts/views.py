from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.posts.models import Post
from application.posts.forms import PostForm


@app.route("/main")
def posts_main():
    return render_template("index.html")

@app.route("/index", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/write/")
@login_required
def posts_form():
    return render_template("posts/write.html", form = PostForm())

@app.route("/posts/", methods=["POST"])
@login_required
def posts_create():

    form = PostForm(request.form)

    if not form.validate():
    	return render_template("posts/write.html", form = form)

    a = Post(request.form.get("content"))
    a.account_id = current_user.id
    db.session().add(a)
  
    db.session().commit()
  
    return redirect(url_for("posts_index"))


