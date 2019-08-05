from application import app, db
from flask import render_template, request, redirect, url_for
from application.posts.models import Post



@app.route("/index", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/write/")
def posts_form():
    return render_template("posts/write.html")

@app.route("/posts/", methods=["POST"])
def posts_create():
    a = Post(request.form.get("content"))
    
    db.session().add(a)
  
    db.session().commit()
  
    return redirect(url_for("posts_index"))
