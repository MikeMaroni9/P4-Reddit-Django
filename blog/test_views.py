from django.test import TestCase

class ViewsTestCase(TestCase):
    def setUp(self):
        # Test User
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Test Post
        self.post = Post.objects.create(title='Test Post', content='This is a test post content', author=self.user, status=1)

        # Test Content
        self.comment = Comment.objects.create(post=self.post, name='Test Commenter', body='This is a test comment body', approved=True)

    def test_home_view(self):
        # Test if the index.html produces correct template
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # Test if post is displayed
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Test if the post_detail.html produces correct page
        response = self.client.get(reverse('postdetail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        # Test if post is displayed
        self.assertContains(response, 'Test Post')

    def test_add_post_view(self):
        # To test adding a post, user has to be logged in.
        self.client.login(username='testuser', password='testpassword')

        # Test if the add_post.html produces correct page
        response = self.client.get(reverse('addpost'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_add_comment_view(self):
        # Test if the add_comment.html produces correct page
        response = self.client.get(reverse('newcomment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

    def test_edit_post_view(self):
        # User has to be logged in to edit the post
        self.client.login(username='testuser', password='testpassword')

        # Test if the edit_post.html produces correct page
        response = self.client.get(reverse('editpost', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_delete_post_view(self):
        # User has to be logged in to delete the page
        self.client.login(username='testuser', password='testpassword')

        # Test if the delete_post.html produces correct page
        response = self.client.get(reverse('deletepost', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')

    def test_post_like_view(self):
        # User has to be logged in to like the post
        self.client.login(username='testuser', password='testpassword')

        # Test if the liking a post produces correct page
        response = self.client.post(reverse('post_like', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse('postdetail', args=[self.post.pk]))