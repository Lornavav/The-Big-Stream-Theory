from .models import Comment, Profile
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            )


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar',]
