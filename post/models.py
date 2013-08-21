from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Categories (models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=240)

    def __unicode__(self):
        return u'%s' % self.name


class Comments(models.Model):
    username = models.CharField(max_length=40, null=True, blank=True)
    mail = models.EmailField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=180)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    validation_key = models.CharField(max_length=30)
    validation = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    item = generic.GenericForeignKey('Content_type', 'Object_id')

    def __unicode__(self):
        return u'Comment: %s' % self.title

    def get_sub(self):
        return Comments.objects.filter(object_id=self.id,
                                       content_type=ContentType.objects.get_for_model(self))


class Posts(models.Model):
    user = models.ForeignKey(User)
    cat = models.ForeignKey(Categories)
    title = models.CharField(max_length=240)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    comments = generic.GenericRelation(Comments)


    def __unicode__(self):
        return self.title