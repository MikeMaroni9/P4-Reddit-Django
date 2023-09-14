from django.test import TestCase
from. forms import CommentForm


class TestCommentForm(TestCase):
    # Test assuming the Comment form is valid
    def test_comment_form_is_valid(self):
        #Checking if both of the fields are filled in and none is left empty.
        form_data = {'body': 'This is a valid comment body.',}
        form = CommentForm(data=form_data)
        #checking if form is valid using assertTrue 
        self.assertTrue(form.is_valid())

    # Test assuming the Comment for is invalid
    def test_comment_form__is_invalid(self):
        ##Checking if one of the fields are left empty 
        form_data = {'body': '',}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_comment_form(self):
        #testing that the only field used is 'body',
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ['body'])