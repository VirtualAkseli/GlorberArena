from application import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from application.posts.models import Post
from application.posts.models import Topic
from application.authentication.models import User
from application.posts.forms import PostForm, ReplyForm, EditForm


@app.route("/main")
def posts_main():
    no_page = request.args.get('page', 1, type=int)
    no_elements = 5
    return render_template("index.html", topics = Topic.query.paginate(no_page, no_elements, False).items, counter = no_page)




@app.route("/posts/write/<theme_num>")
@login_required
def posts_form(theme_num):
    return render_template("posts/write.html", form = PostForm(), theme_id = theme_num)



@app.route("/<theme_num>/posts/", methods=["POST"])
@login_required
def posts_create(theme_num):

    form = PostForm(request.form)

    if not form.validate():
    	return render_template("posts/write.html", form = form, theme_id=theme_num)

    b = Topic(form.topic.data)
    old_topic = Topic.query.filter_by(name=form.topic.data).first()

    if not old_topic:
        b.theme_id = theme_num
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
  
        return redirect(url_for("topic_id", theme_id = theme_num))

    else:
        flash("Topic already taken!")
        return render_template("posts/write.html", form=form, error="Topic already taken!", theme_id=theme_num)

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
    if (post.account_id != current_user.id):
        print("OPERATION NOT ALLOWED!")
        return redirect(url_for("posts_main"))
    post.content = form.content.data

    db.session.add(post)
    db.session.commit()

    return redirect(url_for("post_id", topic_id=post.subject_id))

@app.route("/posts/<post_id>/edit")
@login_required
def post_edit1(post_id):
    return render_template("posts/edit.html", id=post_id, form = EditForm())

@app.route("/posts/delete/<post_id>", methods=["GET", "POST", "DELETE"])
@login_required
def post_delete(post_id):
    
    post = Post.query.filter_by(id=post_id).first()
    if (post.account_id != current_user.id):
        print("OPERATION NOT ALLOWED!")
        return redirect(url_for("posts_main"))
    
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("Page_index"))

@app.route("/posts/<topic_id>")
@login_required
def post_id(topic_id):
    
    topic = Topic.query.filter_by(id=topic_id).first()
    return render_template("posts/single.html", posts = Post.find_matching_topic_for_post(topic_id), subject=topic, form = ReplyForm(), user_id = current_user.id, volume = Post.count_number_of_posts_by_topic(topic_id))


















