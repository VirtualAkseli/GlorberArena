from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators


class PostForm(FlaskForm):
    
    topic = StringField("Title", [validators.Length(min=4)])
    content = TextAreaField("Content", [validators.InputRequired(message="One does not submit an empty message!")])
 
    class Meta:
        csrf = False


class EditForm(FlaskForm):
    
    
    content = TextAreaField("Content", [validators.InputRequired(message="One does not submit an empty message!")])
 
    class Meta:
        csrf = False

class ReplyForm(FlaskForm):
    
    content = TextAreaField("Message", [validators.InputRequired(message="One does not submit an empty message!")])

    class Meta:
        csrf = False
