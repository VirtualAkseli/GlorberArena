from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators


class PostForm(FlaskForm):
    content = TextAreaField("Post content", [validators.InputRequired(message="One does not submit an empty message!")])
 
    class Meta:
        csrf = False
