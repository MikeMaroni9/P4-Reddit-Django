from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.urls import reverse
from .views import AddComment


class ViewsTestCase(TestCase):
    # Common setup
    def setUp(self):
        # user setUp
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.login = self.client.login(
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

    def test_edit_post_view(self):
        # Test if the edit post view renders correctly
        post = self.create_post(title='Test Post Alt')
        post_id = post.pk
        url = reverse('editpost', kwargs={'pk': post_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post.html')

    def test_adding_new_post(self):
        # Test adding a new post and check if it redirects
        response = self.client.post(
            reverse('addpost'), {'title': 'test title', 'content': 'test content'})
        # Check if the response has a redirect status code
        self.assertEqual(response.status_code, 302)

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

    def test_post_like_remove(self):
        # Add the user to the list of likes
        self.post.likes.add(self.user)
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_like', args=[self.post.pk]))
        # Check if the like has been removed
        self.assertFalse(self.post.likes.filter(id=self.user.id).exists())
        # Check if the response redirects to the post detail page
        self.assertRedirects(response, reverse(
            'postdetail', args=[self.post.pk]))

    # Comments

    def test_add_comment_view(self):
        # Test if the add comment view renders correctly
        comment_id = 1
        response = self.client.get(
            reverse('newcomment', kwargs={'pk': comment_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_comment.html')

    def test_add_comment_submission(self):
        response = self.client.post(
            reverse('newcomment', kwargs={'pk': self.post.pk}),
            data={'body': 'Test comment body'}
        )

        # Check if the response is a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect and check the final response
        redirect_url = response.url
        redirect_response = self.client.get(redirect_url)

        # Ensure the final response after the redirect has a status code of 200
        self.assertEqual(redirect_response.status_code, 200)

        # Check if the comment is saved in the database
        self.assertTrue(Comment.objects.filter(
            body='Test comment body').exists())


class ProfileViewTest(TestCase):
    def create_test_user(self):
        # Create a test user
        return User.objects.create_user(username='testuser', password='testpassword')

    def login_user(self):
        # logged in user setUp
        user = self.create_test_user()
        self.client.login(username=user.username, password='testpassword')
        return user

    def test_edit_profile_view_get(self):
        # Create and log in the user
        self.login_user()

        # Make a GET request to the edit_profile view
        response = self.client.get(reverse('edit_profile'))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'edit_profile.html')

    def test_edit_profile_view_post(self):
        # Log in the user
        user = self.login_user()

        # Make a POST request to the edit_profile view with valid data
        data = {'username': 'new_username', 'email': 'new_email@example.com',
                'first_name': 'New', 'last_name': 'User'}
        response = self.client.post(reverse('edit_profile'), data)

        # Check that the user is redirected to the profile page after a successful form submission
        self.assertRedirects(response, reverse('profile'))

    def test_edit_profile_view_post_invalid(self):
        # Log in the user
        self.login_user()

        # Make a POST request to the edit_profile view with invalid data
        data = {'Wrong': 'Wrong'}  # Replace with invalid form data
        response = self.client.post(reverse('edit_profile'), data)
