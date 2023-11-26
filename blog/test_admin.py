
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from blog.models import Post, Comment


class CommentAdminTest(TestCase):
    # Test setUp
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin', password='adminpassword')
        self.client.force_login(self.admin_user)

    def test_approve_comments_action(self):
        # Ttest Post
        post = Post.objects.create(
            title='Test Post',
            author=self.admin_user,
            content='Test Post Content.',
            status=1
        )

        comment = Comment.objects.create(
            # Test Comment
            post=post,
            name='Johnny English',
            body='Comment Body',
            approved=False
        )

        # Admin Action
        data = {'action': 'approve_comments',
                '_selected_action': [comment.id]}
        response = self.client.post(
            reverse('admin:blog_comment_changelist'), data)

        # Refresh the comments  from the db
        comment.refresh_from_db()

        # Is Comment Aproved ?
        self.assertTrue(comment.approved)

        # Check the response
        self.assertEqual(response.status_code, 302)

        # Check if update was applied
        self.assertEqual(Comment.objects.filter(approved=True).count(), 1)

