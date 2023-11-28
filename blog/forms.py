from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


"""
Custom Comment form, using only body section of the form
"""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


"""
Custom form for EditProfile view, taking out the password section of the form.
"""


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = User
        fields = ("username", "email", "first_name", "last_name")
