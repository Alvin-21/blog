from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Blog, Comment, Quotes
from .forms import UpdateProfile, BlogForm, CommentForm
from .. import db

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


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    Function that updates the user's profile.
    """

    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/blogs/new', methods = ['GET','POST'])
@login_required
def new_blog():
    """
    Function that returns the blog page.
    """

    form = BlogForm()

    if form.validate_on_submit():
        username = form.username.data
        title = form.title.data
        description = form.description.data
        new_blog = Blog(blog_username=username, title=title, description=description)
        new_blog.saveBlog()
        return redirect(url_for('main.index'))

    title = 'New Blog'
    return render_template('blog.html', title=title, form=form)


@main.route('/blog/comment/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def new_comment(blog_id):
    """
    Function that returns the comment page.
    """

    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(text=comment, blog_id=blog_id, comment_username=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', blog_id=blog_id))

    title = 'New Comment'
    return render_template('comment.html', title=title, form=form)