from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'thisishardtoguess'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    title = 'Contact Us'
    name = None
    email = None
    subject = None
    inquiry_type = None
    message = None
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        inquiry_type = form.inquiry_type.data
        message = form.message.data
        return redirect(url_for('index'))
    return render_template('contact.html', form=form, name=name, email=email, subject=subject, inquiry_type=inquiry_type, message=message, title=title)

@app.route('/blog')
def list():
    title = 'Blog & Article'
    return render_template('blog-list.html', title=title)

@app.route('/about')
def about():
    title = 'About Us'
    return render_template('about-us.html', title=title)

@app.route('/post/<id>')
def post(id):
    return render_template('blog-page.html', id=id)

@app.route('/movie/<id>')
def movie(id):
    title = 'Movie Details'
    return render_template('movie-details.html', id=id, title=title)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    inquiry_type = SelectField('Inquiry type', choices=[('Advertising', 'Advertising'), ('Site Issues', 'Site Issues')])
    message = TextAreaField('Your Message', validators=[DataRequired()])
    submit = SubmitField('Submit')