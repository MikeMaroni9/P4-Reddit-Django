from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post

class NewPostViewTestCase(TestCase):

    def setUp(self):
        # Create a test client
        self.client = Client()

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Set up data for the form
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
        }

    def test_new_post_view_authenticated_user(self):
        # Test the view when the user is authenticated

        # Make a POST request to the view with valid data
        response = self.client.post(
            reverse('addpost'), data=self.post_data, follow=True)

        # Check if the post is created in the database
        self.assertTrue(Post.objects.filter(title='Test Post').exists())

        # Check if the response contains the expected content
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post content.')

    def test_new_post_view_unauthenticated_user(self):
        # Test the view when the user is not authenticated

        # Log out the test user
        self.client.logout()

        # Make a GET request to the view
        response = self.client.get(reverse('index'))

    # Add more test cases as needed for different scenarios

    def test_new_post_view_form_validation_errors(self):
        # Test the view when the form submission has validation errors

        invalid_post_data = {
            'title': '',  # Invalid title
            'content': 'This is a test post content.',
        }

        # Make a POST request to the view with invalid data
        response = self.client.post(
            reverse('addpost'), data=invalid_post_data)

        # Check if the response contains the expected form validation errors
        self.assertContains(response, 'This field is required.')
        self.assertContains(
            response, 'This is a test post content.')

        # Check that the post is not created in the database
        self.assertFalse(Post.objects.filter(title='Test Post').exists())


