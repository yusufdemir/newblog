from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from django.utils.translation import ugettext
from post.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('cat','title','text')


class CommentForm(forms.Form):
    class Meta:
        model = Comment