from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    """
    Class for updating profile bio.
    """

    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    """
    Class for providing the blog.
    """

    username = StringField("Please enter your username.", validators=[Required()])
    title = StringField('Blog Title',validators=[Required()])
    description = StringField('Description',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """
    Class for provinding comments for the blog.
    """

    username = StringField("Please enter your username.", validators=[Required()])
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Submit')