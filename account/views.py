# Create your views here.
from AptUrl.Helpers import _
from random import choice
from string import letters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from account.models import UserProfile
from forms import RegisterForm, ProfileForm, UserForm
from celery import task
from task import resize_post_image


def register(request):
    if request.method == 'POST':
        data = request.POST.copy()

        # random username
        data['username'] = ''.join([choice(letters) for i in xrange(30)])
        form = RegisterForm(data)

        if form.is_valid():
            user = form.save()
            messages.success(request, _("Registration Success. Please Sing In"))
            return HttpResponseRedirect('/index/')
    else:
        form = RegisterForm()

    return render_to_response('login.html', {'form': form},
                              context_instance=RequestContext(request))


@login_required
def getProfile(request):
    # get user profile
    user = request.user
    profile = user.get_profile()


    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=profile)

        user_form = UserForm(request.POST,
                             instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

            resize_post_image.delay(profile_form.save())

            messages.success(request, _("Profile updated succesfully."))
            return redirect('index')
    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    return render(request, 'profile.html', {
        'formProfile': profile_form,
        'formUser': user_form
    })

