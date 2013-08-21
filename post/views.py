# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from post.models import *


def index(request):
    posts = Posts.objects.all()
    comments_all = Comments.objects.all()

    #def get_sub(self):
     #   comments_all.filter(object_id=self.id, content_type=ContentType.objects.get_for_model(self))

    return render_to_response("index.html", {'posts': posts, 'comments': comments_all},
                              context_instance=RequestContext(request))


def postDetailView(request, post_id):
    posts = Posts.objects.filter(pk=post_id)
    ctx = {
        'posts': posts
    }
    return render(request, 'detail.html', ctx)