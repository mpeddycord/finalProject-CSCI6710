from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
import sqlalchemy as sa
from app import db

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    inquiry_type = SelectField('Inquiry type', choices=[('Advertising', 'Advertising'), ('Site Issues', 'Site Issues')])
    message = TextAreaField('Your Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmailSubscribeForm(FlaskForm):
    email = StringField('Email Address', validators=[Email()], render_kw={"placeholder": "Your email address..."})
    submit = SubmitField('Subscribe')
