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
        # model = Profilis
        # fields = ['username', 'description']
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    description = forms.CharField()

    class Meta:
        model = Profilis
        fields = ['nuotrauka', 'description']

class AddPostForm(forms.ModelForm):
    nuotrauka = forms.ImageField()
    description = forms.CharField()
    class Meta:
        model = Post
        fields = ['nuotrauka', 'description']
        widgets = {
            'nuotrauka': forms.FileInput(attrs={
                'id': 'nuotraukos_id',
            })
        }
# class NewPostForm(forms.Form):
#     nuotrauka = forms.ImageField()
#     description = forms.CharField()
#     class Meta:
#         model = Post
#         fields = ['nuotrauka', 'description' ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'