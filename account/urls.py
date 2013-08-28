from django.conf.urls import patterns, url
from django.contrib.auth.views import *

urlpatterns = patterns("account.views",
    url(r'^register/', 'register', name='RegistrationForm'),
    url(r'^profile/$','getProfile', name="getProfile"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login',{'template_name': 'account/login.html'},
        name="login"),
    url(r'^logout/$', 'logout',{'next_page': '/index/'},
        name="logout"),
)