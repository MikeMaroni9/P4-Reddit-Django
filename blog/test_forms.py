from django.test import TestCase
from . forms import CommentForm, EditProfileForm

class TestCommentForm(TestCase):
    # Test assuming the Comment form is valid
    def test_comment_form_is_valid(self):
        # Checking if comment field is filled in and is not left empty.
        form_data = {'body': 'This is a valid comment body.', }
        form = CommentForm(data=form_data)
        # checking if form is valid using assertTrue
        self.assertTrue(form.is_valid())

    # Test assuming the Comment for is invalid
    def test_comment_form__is_invalid(self):
        # Checking if comment field is left empty
        form_data = {'body': '', }
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_comment_form(self):
        # testing that the only field used in comment section is 'body',
        form = CommentForm()
        self.assertIn('body', form.fields)
        self.assertEqual(len(form.fields), 1)

class EditProfileFormTestCase(TestCase):

    def test_profile_edit_form(self):
        # As the scope wise for this project only necessary field editing
        # profile is name field, checking if the name field can be left empty.
        form = EditProfileForm({'username': ''})
        # Checking if != form is valid
        self.assertFalse(form.is_valid())
        # checking if username is in dictionary of form errors
        self.assertIn('username', form.errors.keys())
        # Checking if the error msg on the field = "This field is required."
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_fields_are_explicit_in_edit_profile_form(self):
        # Initializing empty form
        form = EditProfileForm()
        # checking the meta fields, that the order is correct and that the
        #  error will be shows if someone alters the forms model later on.
        self.assertEqual(form.Meta.fields, (
                         'username', 'email', 'first_name', 'last_name'))


