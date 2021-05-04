import unittest
from app.models import User, Blog, Comment
from app import db

class BlogTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Blog Class.
    """

    def tearDown(self):
        """
        Cleans up after each test case has run.
        """

        User.query.delete()
        Blog.query.delete()
        
    def setUp(self):
        """
        Set up method that will run before every Test.
        """

        self.new_user = User(username="john", email="john@gmail.com", pass_secure="trial1")

        self.new_blog = Blog(title="business blog", description="asdfghjkl")

    def test_check_instance_variables(self):
        """
        Test case to check if the values of variables are correctly being placed.
        """

        self.assertEquals(self.new_blog.title, "business blog")
        self.assertEquals(self.new_blog.description, "asdfghjkl")
        self.assertEquals(self.new_blog.user_id, self.new_user.id)

    def test_save_blog(self):
        """
        Test case to check if the blog is saved to the database.
        """

        
        self.new_blog.saveBlog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_delete_blog(self):
        """
        Test case to check if the blog is removed from the database.
        """

        self.new_blog.saveBlog()
        self.new_blog.deleteBlog()
        self.assertTrue(len(Blog.query.all())==0)

    def test_get_blog(self):
        """
        Test case to check if user's blogs can be returned.
        """

        self.new_blog.saveBlog()
        got_blog = Blog.getBlogs(self.new_blog.user_id)
        self.assertTrue(len(got_blog) == 1)

    def test_get_all_blogs(self):
        """
        Test case to check if all blogs can be returned.
        """

        self.new_blog.saveBlog()
        got_blog = Blog.getallBlogs()
        self.assertTrue(len(got_blog) == 1)

    