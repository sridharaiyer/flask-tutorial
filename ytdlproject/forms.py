from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from wtforms import ValidationError

class DownloadMP3(FlaskForm):
    videourl = StringField('Youtube Video URL', validators=[DataRequired(),URL()])
    submit = SubmitField('Submit')
