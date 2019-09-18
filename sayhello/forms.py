from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), length(1, 20)])
    body = TextAreaField('Message', validators=[
                         DataRequired(), length(1, 200)])
    submit = SubmitField()
