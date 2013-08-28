from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("post.views",
    url(r'^$', 'index', name='home'),
    url(r'^index/$', 'index', name='index'),
    url(r'^send-post/$', 'sendPost', name='sendPost'),
    url(r'^mypost/$', 'mypost', name='myPost'),
    url(r'^detail/(?P<post_id>\d+)/$', 'postDetailView', name='detail'),
    url(r'^cat/(?P<cat_id>\d+)/$','catView', name="category"),
)