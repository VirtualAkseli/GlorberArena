from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, validators


class ThemeForm(FlaskForm):
    
    name = StringField("A descriptive name for the general theme of discussion", [validators.Length(min=5)])
    
    class Meta:
        csrf = False

