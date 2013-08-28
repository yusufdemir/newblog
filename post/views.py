# Create your views here.
from AptUrl.Helpers import _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from post.forms import PostForm
from post.models import *
from django.views.decorators.http import require_http_methods

def index(request):
    posts = Post.objects.all()
    ctx={'posts': posts,}
    return render(request, "index.html", ctx )


def postDetailView(request, post_id):

    posts = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)

    rootComments=comments.filter(content_type_id=ContentType.objects.get_for_model(Post))
    subComments = comments.filter(content_type_id=ContentType.objects.get_for_model(Comment))
    ctx = {
        'posts': posts, 'rootComments': rootComments, 'subComments': subComments
    }
    return render(request, 'post/detail.html', ctx)


def catView(request, cat_id):
    post = Post.objects.filter(cat__pk=cat_id)
    ctx = {
        'posts': post
    }
    return render(request, 'index.html', ctx)

@login_required
def mypost(request):
    post = Post.objects.filter(user__pk =request.user.id)
    ctx = {
        'post': post
    }
    return render(request, 'index.html', ctx)


@login_required
def sendPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save(commit=True)
            messages.success(request, _("Send Post Succesfully."))
            return redirect('index')
    else:
        form = PostForm()

    return render(request, 'post/sendpost.html', {'form': form})


def commentForm(request):
    if request.method== 'POST':
        form = commentForm(request.POST)
        if form.is_valid():

            form.save()

        else:
            form = commentForm()

        return render(request, 'post/detail.html',{'form': form})

