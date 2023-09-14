from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class ModelTestCase(TestCase):

    #Setting up tests
    def setUp(self):
        # creating a test user and a test content
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', author=self.user, content='This is a test post content', status=1)
        self.comment = Comment.objects.create(post=self.post, name='Test Commenter', body='This is a test comment body', approved=True)

    #testing if the post can be created
    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test post content')
        self.assertEqual(post.status, 1)

    #testing if the comments can be created
    def test_comment_creation(self):
        comment = Comment.objects.get(name='Test Commenter')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.body, 'This is a test comment body')
        self.assertTrue(comment.approved)