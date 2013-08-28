from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Category (models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=240)

    def __unicode__(self):
        return u'%s' % self.name


class Comment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    username = models.CharField(max_length=40, null=True, blank=True)
    mail = models.EmailField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=180)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    validation_key = models.CharField(max_length=30)
    validation = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    post_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    item = generic.GenericForeignKey('Content_type', 'Object_id')

    def __unicode__(self):
        return u'Comment: %s' % self.title


class Post(models.Model):
    user = models.ForeignKey(User)
    cat = models.ForeignKey(Category)
    title = models.CharField(max_length=240)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = generic.GenericRelation(Comment)

    def __unicode__(self):
        return self.title