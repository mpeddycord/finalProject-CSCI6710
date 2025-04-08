from flask import Flask, render_template, redirect, url_for
import sqlalchemy as sa
from app import db
from app.main.forms import ContactForm
from app.models import User
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/contact', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    return render_template('contact.html', form=form, name=name, email=email, subject=subject, inquiry_type=inquiry_type, message=message, title=title)

@bp.route('/blog')
def list():
    title = 'Blog & Article'
    user = db.first_or_404(sa.select(User))
    return render_template('blog-list.html', user=user, title=title)

@bp.route('/about')
def about():
    title = 'About Us'
    return render_template('about-us.html', title=title)

@bp.route('/post/<id>')
def post(id):
    return render_template('blog-page.html', id=id)

@bp.route('/movie/<id>')
def movie(id):
    title = 'Movie Details'
    return render_template('movie-details.html', id=id, title=title)