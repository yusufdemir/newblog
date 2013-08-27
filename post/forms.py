from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from django.utils.translation import ugettext
from post.models import *


class postForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('cat','title','text')


class commentForm(forms.Form):
    class Meta:
        model = Comments