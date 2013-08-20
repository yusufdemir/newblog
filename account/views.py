# Create your views here.
from AptUrl.Helpers import _
from random import choice
from string import letters
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import RegisterForm


def register(request):
    if request.method == 'POST':
        data = request.POST.copy()

        # random username
        data['username'] = ''.join([choice(letters) for i in xrange(30)])
        form = RegisterForm(data)

        if form.is_valid():
            user = form.save()
            messages.success(request, _("Registration Succes."))
            return HttpResponseRedirect('/index/')
    else:
        form = RegisterForm()

    return render_to_response('login.html', {'form': form},
                              context_instance=RequestContext(request))