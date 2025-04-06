from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact-page.html')

@app.route('/blog')
def list():
    return render_template('blog-list.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/post/<id>')
def post(id):
    return render_template('blog-page.html', id=id)

@app.route('/movie/<id>')
def movie(id):
    return render_template('movie-details.html', id=id)