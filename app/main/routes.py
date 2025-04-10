from flask import Flask, render_template, redirect, url_for, request
import sqlalchemy as sa
from app import db
from app.main.forms import ContactForm, EmailSubscribeForm
from app.models import Post, Movie, MovieMoment, MovieReason
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
def index():
    top_movie = Movie.query.where(Movie.position == 'top').first()
    middle_movies_1 = Movie.query.where(Movie.position == 'middle').limit(3)
    middle_movies_2 = Movie.query.where(Movie.position == 'middle').offset(3).limit(2)
    middle_movies_3 = Movie.query.where(Movie.position == 'middle').offset(5).limit(3)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    bottom_movies_2 = Movie.query.where(Movie.position == 'bottom').offset(4).limit(4)
    email = None
    form = EmailSubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('main.index'))
    return render_template('index.html', top_movie=top_movie, middle_movies_1=middle_movies_1, middle_movies_2=middle_movies_2, middle_movies_3=middle_movies_3, bottom_movies_1=bottom_movies_1, bottom_movies_2=bottom_movies_2, form=form, email=email)

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
    subscribe_email = None
    subscribe_form = EmailSubscribeForm()
    if form.validate_on_submit():
        subscribe_email = subscribe_form.email.data
        return redirect(url_for('main.index'))
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    return render_template('contact.html', form=form, name=name, email=email, subject=subject, inquiry_type=inquiry_type, message=message, title=title, bottom_movies_1=bottom_movies_1, subscribe_form=subscribe_form, subscribe_email=subscribe_email)

@bp.route('/blog', methods=['GET', 'POST'])
def list():
    title = 'Blog & Article'
    other_movies = Movie.query.where(Movie.position == 'other').limit(3)
    page = request.args.get('page', 1, type=int) 
    posts = Post.query.paginate(page=page, per_page=5, error_out=False)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    email = None
    form = EmailSubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('main.index'))
    return render_template('blog-list.html', posts=posts, title=title, other_movies=other_movies, bottom_movies_1=bottom_movies_1, pagination=posts, form=form, email=email)

@bp.route('/about', methods=['GET', 'POST'])
def about():
    title = 'About Us'
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    email = None
    form = EmailSubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('main.index'))
    return render_template('about-us.html', title=title, bottom_movies_1=bottom_movies_1, form=form, email=email)

@bp.route('/post/<id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.get(id)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    email = None
    form = EmailSubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('main.index'))
    return render_template('blog-page.html', id=id, post=post, bottom_movies_1=bottom_movies_1, form=form, email=email)

@bp.route('/movie/<id>', methods=['GET', 'POST'])
def movie(id):
    title = 'Movie Details'
    movie = Movie.query.get(id)
    other_movies = Movie.query.where(Movie.position == 'other').limit(3)
    bottom_movies_1 = Movie.query.where(Movie.position == 'bottom').limit(4)
    movie_moments = MovieMoment.query.where(MovieMoment.movie_id == id)
    pros = MovieReason.query.filter(MovieReason.type == 'P', MovieReason.movie_id == id).limit(5)
    cons = MovieReason.query.filter(MovieReason.type == 'C', MovieReason.movie_id == id).limit(3)
    email = None
    form = EmailSubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        return redirect(url_for('main.index'))
    return render_template('movie-details.html', id=id, title=title, movie=movie, other_movies=other_movies, movie_moments=movie_moments, bottom_movies_1=bottom_movies_1, pros=pros, cons=cons , form=form, email=email)