from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.authentication.models import User
from application.authentication.forms import LoginForm, UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("authentication/login.html", form = LoginForm())

    form = LoginForm(request.form)
    counter = 0
    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("authentication/login.html", form = form,
                                error = "Check your credentials")

    login_user(user)
    return redirect(url_for("Page_index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("authentication/register.html", form = UserForm())
 
    form = UserForm(request.form)
    b = User(form.username.data)
    usern = User.query.filter_by(username=form.username.data).first()
    nick = User.query.filter_by(name=form.name.data).first()
    if not usern and not nick:
        b.name = form.name.data
        b.username = form.username.data
        b.password = form.password.data

        db.session().add(b)
        db.session().commit()
    
        login_user(b)
    else:
        if usern and nick:
            return render_template("authentication/register.html", form = form, error = "Username and nick taken")
        if usern:
            return render_template("authentication/register.html", form = form, error = "Username taken")
        if nick:
            return render_template("authentication/register.html", form = form, error = "Nick taken")

    return redirect(url_for("Page_index"))

    


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
