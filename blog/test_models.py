from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.urls import reverse

class ModelsTestCase(TestCase):
    def setUp(self):
        # user setUp
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_post_model(self):
        # new post setUp
        post = Post.objects.create(
            title='Test Post',
            author=self.user,
            content='This is a test post content.',
            status=1
        )

        # Check if the Post is saved correctly
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test post content.')
        self.assertEqual(post.status, 1)

        # Test the number_of_likes method
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment_model(self):
        # Test creating a new Comment
        post = Post.objects.create(
            title='Test Post',
            author=self.user,
            content='This is a test post content.',
            status=1
        )

        comment = Comment.objects.create(
            post=post,
            name='Test Commenter',
            body='This is a test comment body.',
            approved=True
        )

        # Check if the Comment is saved correctly
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.name, 'Test Commenter')
        self.assertEqual(comment.body, 'This is a test comment body.')
        self.assertTrue(comment.approved)


