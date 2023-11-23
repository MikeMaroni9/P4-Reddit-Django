from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class SignupPageTestCase(TestCase):
    # setUp
    def setUp(self):
        self.client = Client()
        self.user_data = {
            'username': 'user',
            'password1': 'password111',
            'password2': 'password111',
        }

    def test_signup_page_loads(self):
        # Loads Successfuly ?
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sign Up')

    def test_signup_form_submission(self):

        # Make a POST request to the signup / Valid Data
        response = self.client.post(
            reverse('account_signup'), data=self.user_data)

        # Check if the user gets created
        self.assertTrue(User.objects.filter(username='user').exists())

    def test_invalid_signup_form_submission(self):
        # Checking Invalid Sign Up

        # Invalid User Name Provided
        invalid_user_data = {
            'username': '',  # Invalid username
            'password1': 'password111',
            'password2': 'password111',
        }
        response = self.client.post(
            reverse('account_signup'), data=invalid_user_data)

        # Checking Response Code
        self.assertEqual(response.status_code, 200)

        # Checking if the response code is correct
        self.assertContains(response, 'This field is required.')


