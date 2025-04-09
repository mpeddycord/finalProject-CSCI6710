from flask import Flask, render_template, redirect, url_for
import sqlalchemy as sa
from app import db
from app.main.forms import ContactForm
from app.models import Post, Movie
from app.main import bp

@bp.route('/')
def index():
    middle_movies_1 = Movie.query.where(Movie.position == 'middle').limit(3)
    middle_movies_2 = Movie.query.where(Movie.position == 'middle').offset(3).limit(2)
    middle_movies_3 = Movie.query.where(Movie.position == 'middle').offset(5).limit(3)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    bottom_movies_2 = Movie.query.where(Movie.position == 'bottom').offset(4).limit(4)
    return render_template('index.html', middle_movies_1=middle_movies_1, middle_movies_2=middle_movies_2, middle_movies_3=middle_movies_3, bottom_movies_1=bottom_movies_1, bottom_movies_2=bottom_movies_2)

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
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    return render_template('contact.html', form=form, name=name, email=email, subject=subject, inquiry_type=inquiry_type, message=message, title=title, bottom_movies_1=bottom_movies_1)

@bp.route('/blog')
def list():
    title = 'Blog & Article'
    other_movies = Movie.query.where(Movie.position == 'other').limit(3)
    posts = Post.query.order_by(Post.date_created.desc()).all()
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)

    return render_template('blog-list.html', posts=posts, title=title, other_movies=other_movies, bottom_movies_1=bottom_movies_1)

@bp.route('/about')
def about():
    title = 'About Us'
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)

    return render_template('about-us.html', title=title, bottom_movies_1=bottom_movies_1)

@bp.route('/post/<id>')
def post(id):
    post = Post.query.get(id)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)

    return render_template('blog-page.html', id=id, post=post, bottom_movies_1=bottom_movies_1)

@bp.route('/movie/<id>')
def movie(id):
    title = 'Movie Details'
    movie = Movie.query.get(id)
    other_movies = Movie.query.where(Movie.position == 'other').limit(3)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    return render_template('movie-details.html', id=id, title=title, movie=movie, other_movies=other_movies, bottom_movies_1=bottom_movies_1)