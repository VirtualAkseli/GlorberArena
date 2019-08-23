from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.posts.models import Post
from application.posts.subject import Topic
from application.authentication.models import User
from application.posts.forms import PostForm, ReplyForm, EditForm


@app.route("/main")
def posts_main():
    return render_template("index.html", topics = Topic.query.all())



@app.route("/index", methods=["GET"])
@login_required
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

    b = Topic(form.topic.data)
    db.session().add(b)
    db.session().commit()
    Subject = Topic.query.filter_by(name=form.topic.data).first()

    a = Post(request.form.get("content"))
    a.topic = form.topic.data
    a.author = current_user.name
    a.account_id = current_user.id
    a.subject_id = Subject.id
    db.session().add(a)
  
    db.session().commit()
  
    return redirect(url_for("posts_main"))

@app.route("/posts/reply/<topic_id>", methods=["POST"])
@login_required
def posts_reply(topic_id):
    form = ReplyForm(request.form)
    subject = Topic.query.filter_by(id=topic_id).first()

    a = Post(request.form.get("content"))
    a.topic = subject.name
    a.author = current_user.name
    a.account_id = current_user.id
    a.subject_id = subject.id
    db.session().add(a)
  
    db.session().commit()
  
    return redirect(url_for("post_id", topic_id=topic_id))

@app.route("/posts/<post_id>", methods=["POST"])
@login_required
def post_edit(post_id):
    form = EditForm(request.form)
    post = Post.query.filter_by(id=post_id).first()
    post.content = form.content.data

    db.session.add(post)
    db.session.commit()

    return redirect(url_for("post_id", topic_id=post.subject_id))

@app.route("/posts/<post_id>/edit")
@login_required
def post_edit1(post_id):
    return render_template("posts/edit.html", id=post_id, form = EditForm())


@app.route("/posts/<topic_id>")
@login_required
def post_id(topic_id):
    
    topic = Topic.query.filter_by(id=topic_id).first()
    return render_template("posts/single.html", posts = Post.find_matching_topic_for_post(topic_id), subject=topic, form = ReplyForm(), user_id = current_user.id)


















