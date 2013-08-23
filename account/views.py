# Create your views here.
from AptUrl.Helpers import _
from random import choice
from string import letters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms import RegisterForm, userProfileForm


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
def profileFormView(request):
    if request.method == 'POST':
        form = userProfileForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            userprofile_id=request.user.id
            return HttpResponseRedirect('/profile/')
        return render_to_response("profile.html", {'form': form},

                                  context_instance=RequestContext(request))

    formProfile = userProfileForm(initial={'phone':request.user.id})


    return render(request, "profile.html", {'formProfile': formProfile})