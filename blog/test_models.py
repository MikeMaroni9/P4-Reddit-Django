from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.urls import reverse


class ModelsTestCase(TestCase):
    def setUp(self):
        # User setUp
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def create_post(self, title="Test Post", content="Test Post Content.", status=1):
        return Post.objects.create(
            title=title, author=self.user, content=content, status=status
        )

    def test_post_model(self):
        # New post setUp
        post = self.create_post()

        # Check if the Post is saved correctly
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, "Test Post Content.")
        self.assertEqual(post.status, 1)

        # Test the number_of_likes method
        self.assertEqual(post.number_of_likes(), 0)

    def test_post_string_method_returns_name(self):
        # Testing the string method of the Post model
        post = self.create_post()
        self.assertEqual(str(post), "Test Post")

    def test_comment_model(self):
        # Test creating a new Comment
        post = self.create_post()
        comment = Comment.objects.create(
            post=post, name="Test Commenter", body="Test Comment Body.", approved=True
        )

        # Check if the Comment is saved correctly
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.name, "Test Commenter")
        self.assertEqual(comment.body, "Test Comment Body.")
        self.assertTrue(comment.approved)

    def test_comment_string_method(self):
        post = self.create_post()
        comment = Comment.objects.create(
            post=post,
            name="testUser",
            body="Test Comment Body",
        )
        expected_result = f"Comment {comment.body} by {comment.name}"
        self.assertEqual(str(comment), expected_result)
