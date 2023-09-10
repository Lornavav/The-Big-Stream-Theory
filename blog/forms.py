from .models import Comment, Post
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CommentForm(forms.ModelForm):
    """
    Form where end users can leave comments
    """
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    """
    Form for staff to add blogpost on the front end
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True

    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'cast',
            'content',
            'featured_image',
            'excerpt',
            'status',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'cast': forms.TextInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '600px'}}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
