from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib import admin
from NewBlog import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # account app url
    url(r'^', include('account.urls')),

    # post app url
    url(r'^', include('post.urls')),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

