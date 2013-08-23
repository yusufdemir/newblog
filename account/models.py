from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    userProfile= models.OneToOneField(User)
    image = models.ImageField(upload_to='photo/', default='photo/None/no-img.jpg')
    phone = models.CharField(max_length=10, blank=True,)
    job = models.CharField(max_length=40, blank=True,)
    validation_key = models.CharField(max_length=24, null=True, blank=True)
    validation = models.BooleanField(default=True)