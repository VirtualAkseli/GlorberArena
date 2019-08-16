from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators


class PostForm(FlaskForm):
    
    topic = StringField("Title")
    content = TextAreaField("Content", [validators.InputRequired(message="One does not submit an empty message!")])
 
    class Meta:
        csrf = False

class ReplyForm(FlaskForm):
    
    content = TextAreaField("Message")

    class Meta:
        csrf = False
