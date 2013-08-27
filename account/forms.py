from django.contrib.auth.forms import UserCreationForm, User
from django import forms
from django.utils.translation import ugettext
from account.models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', max_length=75)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError(ugettext('This email address already exists. Did you forget your password?'))
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image', 'gender')


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # not required
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name')