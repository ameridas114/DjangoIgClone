from .models import PostComment, Profilis
from django import forms
from django.contrib.auth.models import User
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('content', 'post', 'commenter',)
        widgets = {'post': forms.HiddenInput(), 'commenter': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    description = forms.CharField()

    class Meta:
        model = Profilis
        fields = ['nuotrauka', 'description']

