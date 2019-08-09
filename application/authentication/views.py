from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.authentication.models import User
from application.authentication.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("authentication/login.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("authentication/login.html", form = form,
                                error = "Check your credentials")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))