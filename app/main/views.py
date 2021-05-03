from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required
from ..models import User, Blog, Comment, Quotes

# Views
@main.route('/')
def index():
    '''
    Function that returns the index page and its data.
    '''

    title = 'Home'

    return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    """
    Function that returns the user's profile page.
    """

    user = User.query.filter_by(username=uname).first()
    blogs = Blog.query.filter_by(user_id=User.id).all()
    comments = Comment.query.filter_by(blog_id=Blog.id).all()
    
    title = f"{uname.capitalize()}"

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user, title=title, blogs=blogs, comments=comments)