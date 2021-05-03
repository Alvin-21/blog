from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    This class defines new User objects.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    """
    Class for defining blogs.
    """

    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_username = db.Column(db.String(255), db.ForeignKey("users.username"))
    title = db.Column(db.String(255))
    description = db.Column(db.Text, index = True)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def saveBlog(self):
        db.session.add(self)
        db.session.commit()

    def deleteBlog(self):
        db.session.delete(self)
        db.session.commit()    

    @classmethod
    def getBlogs(cls, username):
        blogs = Blog.query.filter_by(blog_username=username).order_by(Blog.time.desc()).all()
        return blogs

    @classmethod
    def getallBlogs(cls):
        blogs = Blog.query.order_by(Blog.time.desc()).all()
        return blogs

class Comment(db.Model):
    """
    Class for defining comments for blog posts.
    """

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_username = db.Column(db.String(255), db.ForeignKey("users.username"))
    text = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        """
        Method for saving the comments to the database.
        """

        db.session.add(self)
        db.session.commit()

    def deleteComment(self):
        """
        Method for deleting the comments from the database.
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        """
        Method for getting the comments.
        """
        
        comments = Comment.query.filter_by(blog_id=id).all()
        return  comments

class Quotes:
    '''
    Class for defining Quote Objects.
    '''

    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote