from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.static import static
from django.contrib import admin
from NewBlog import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'post.views.index', name='home'),
    url(r'^index/$', 'post.views.index', name='index'),
    url(r'^register/', 'account.views.register', name='RegistrationForm'),
    #url(r'^sendpost/', 'post.views.sendPost', name='sendPostForm'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/index/'}),
    url(r'^profile/$','account.views.getProfile'),
    url(r'^send-post/$', 'post.views.sendPost', name='sendPost'),
    url(r'^detail/(?P<post_id>\d+)/$', 'post.views.postDetailView', name='detail'),
    url(r'^cat/(?P<cat_id>\d+)/$','post.views.catView'),

    # url(r'^NewBlog/', include('NewBlog.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)