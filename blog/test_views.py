from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.urls import reverse

class ViewsTestCase(TestCase):
    def setUp(self):
        # user setUp
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        # test post setUp
        self.post = self.create_post()
        # comment setUp
        self.comment = self.create_comment(self.post)

    def create_post(self, title='Test Post', content='This is a testpost content', status=1):
        # post setUp
        return Post.objects.create(title=title, content=content, author=self.user, status=status)

    def create_comment(self, post, name='Test Commenter', body='This is a test comment body', approved=True):
        # comment setUp
        return Comment.objects.create(post=post, name=name, body=body, approved=approved)

    def login_user(self):
        # logged in user setUp
        self.client.login(username='testuser', password='testpassword')

    def test_home_view(self):
        # Test if the home view renders correctly and displays the test post
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Test if the post detail view renders correctly and displays the test post
        self.login_user()
        response = self.client.get(reverse('postdetail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_edit_post_page(self):
        # Test if the edit post page renders correctly
        post = self.create_post(title='Test Post Alt')
        post_id = post.pk
        url = reverse('editpost', kwargs={'pk': post_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_edit_post_view(self):
        # Test if the edit post view renders correctly
        self.login_user()
        response = self.client.get(reverse('editpost', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_add_post_view(self):
        # Test if the add post view renders correctly
        self.login_user()
        response = self.client.get(reverse('addpost'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_adding_new_post(self):
        # Test adding a new post and check if it exists in the database
        response = self.client.post(
            reverse('addpost'), {'title': 'test title'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Post.objects.filter(title='test title').exists())

    def test_add_comment_view(self):
        # Test if the add comment view renders correctly
        comment_id = 1
        response = self.client.get(
            reverse('newcomment', kwargs={'pk': comment_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

    def test_delete_post_view(self):
        # Test if the delete post view renders correctly
        self.login_user()
        response = self.client.get(reverse('deletepost', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_post.html')

    def test_deleting_a_post(self):
        # Test deleting a post and check if the user is redirected to the index page
        post = self.create_post(title='Test Post DELETE')
        post_id = post.pk
        response = self.client.get(f'/detail/{post_id}/delete')
        self.assertEqual(response.status_code, 200)
        form_submission_url = reverse('deletepost', args=[post_id])
        response = self.client.post(form_submission_url)
        self.assertRedirects(response, reverse('index'))

    def test_post_like_view(self):
        # Test liking a post and check if the user is redirected to the post detail page
        self.login_user()
        response = self.client.post(reverse('post_like', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, reverse(
            'postdetail', args=[self.post.pk]))


