from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from django.utils.translation import ugettext
from post.models import Posts

@login_required
class postForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('cat','title','text')

        def __unicode__(self):
            return self.title