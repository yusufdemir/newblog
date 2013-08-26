# Create your views here.
from AptUrl.Helpers import _
from django.contrib import messages
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from post.forms import postForm
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
    comments = Comments.objects.filter(post_id=post_id)

    rootComments=comments.filter(content_type_id=ContentType.objects.get_for_model(Posts))
    subComments = comments.filter(content_type_id=ContentType.objects.get_for_model(Comments))
    ctx = {
        'posts': posts, 'rootComments':rootComments, 'subComments': subComments
    }
    return render(request, 'detail.html', ctx)


def catView(request, cat_id):
    post = Posts.objects.filter(cat__pk = cat_id)
    ctx = {
        'posts': post
    }
    return render(request, 'index.html', ctx)


def sendPost(request):
    user=request.user
    profile = user.get_profile()

    if request.method == 'POST':
        form=postForm(instance=user)

        if form.is_valid():
            form.save()

            messages.success(request, _("Send Post Succesfuly."))
            return redirect('detail')

    else:
        form=postForm
    return render(request,'detail.html',{'form': form})