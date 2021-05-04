import unittest
from app.models import User, Blog, Comment
from app import db

class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment Class.
    """

    def tearDown(self):
        """
        Cleans up after each test case has run.
        """

        User.query.delete()
        Blog.query.delete()
        Comment.query.delete()
        
    def setUp(self):
        """
        Set up method that will run before every Test.
        """

        self.new_user = User(username="john", email="john@gmail.com", pass_secure="trial1")
        self.new_blog = Blog(title="business blog", description="asdfghjkl")
        self.new_comment = Comment(text="good blog")

    def test_check_instance_variables(self):
        """
        Test case to check if the values of variables are correctly being placed.
        """

        self.assertEquals(self.new_comment.text, "good blog")
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id)

    def test_save_comment(self):
        """
        Test case to check if the comment is saved to the database.
        """

        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_delete_blog(self):
        """
        Test case to check if the blog is removed from the database.
        """

        self.new_comment.save_comment()
        self.new_comment.deleteComment()
        self.assertTrue(len(Blog.query.all())==0)

    def test_get_comment(self):
        """
        Test case to check if comments can be returned.
        """

        self.new_blog.saveBlog()
        self.new_comment.save_comment()
        got_comment = Comment.get_comments(self.new_comment.blog_id)
        self.assertTrue(len(got_comment) == 1)