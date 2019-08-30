from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.posts.models import Post
from application.posts.subject import Topic
from application.authentication.models import User
from application.posts.forms import PostForm, ReplyForm, EditForm


@app.route("/profiles/<account_name>")
@login_required
def profile_view(account_name):
    
    return render_template("profiles/profile.html", account=current_user, posts=User.find_posts_by_user(current_user.id), no_posts=User.find_quant_of_posts_by_user(current_user.id))
















