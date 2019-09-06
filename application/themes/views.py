from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.posts.models import Topic
from application.themes.models import Theme
from application.authentication.models import User

from application.themes.forms import ThemeForm

@app.route("/index")
def Page_index():
    no_page = request.args.get('page', 1, type=int)
    no_elements = 10
    return render_template("Themes/main_index.html", themes = Theme.query.paginate(no_page, no_elements, False).items, counter = no_page, form=ThemeForm())



@app.route("/<theme_id>")
@login_required
def topic_id(theme_id):
    no_page = request.args.get('page', 1, type=int)
    no_elements = 5
    theme_name = Theme.find_name_for_theme(theme_id)
    
    return render_template("index.html", name=theme_name[0], theme_id = theme_id, topics = Topic.query.filter_by(theme_id=theme_id).paginate(no_page, no_elements, False).items, counter = no_page)

@app.route("/new_theme/", methods=["POST"])
@login_required
def theme_create():
    if not (current_user.admin == 1):
        errmsg = "Warning! Unauthorized operation! Report your findings to administrators immediately"
        return redirect(url_for("Page_index", error = errmsg))
    form = ThemeForm(request.form)

    if not form.validate():
        return render_template("Themes/main_index.html", form=form)

    a = Theme(form.name.data)
    db.session().add(a)
    db.session.commit()

    return redirect(url_for("Page_index"))
