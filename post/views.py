# Create your views here.
from AptUrl.Helpers import _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from post.forms import postForm
from post.models import *
from django.views.decorators.http import require_http_methods

def index(request):
    posts = Posts.objects.all()
    comments_all = Comments.objects.all()

    #def get_sub(self):
     #   comments_all.filter(object_id=self.id, content_type=ContentType.objects.get_for_model(self))
    ctx={'posts': posts, 'comments': comments_all}
    return render(request, "index.html", ctx )


def postDetailView(request, post_id):

    posts = Posts.objects.filter(pk=post_id)
    comments = Comments.objects.filter(post_id=post_id)

    rootComments=comments.filter(content_type_id=ContentType.objects.get_for_model(Posts))
    subComments = comments.filter(content_type_id=ContentType.objects.get_for_model(Comments))
    ctx = {
        'posts': posts, 'rootComments': rootComments, 'subComments': subComments
    }
    return render(request, 'detail.html', ctx)


def catView(request, cat_id):
    post = Posts.objects.filter(cat__pk=cat_id)
    ctx = {
        'posts': post
    }
    return render(request, 'index.html', ctx)


@login_required
def sendPost(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save(commit=True)
            messages.success(request, _("Send Post Succesfully."))
            return redirect('index')
    else:
        form = postForm()

    return render(request, 'sendpost.html', {'form': form})


def commentForm(request):
    if request.method== 'POST':
        form = commentForm(request.POST)
        if form.is_valid():

            form.save()

        else:
            form = commentForm()

        return render(request, 'detail.html',{'form': form})

