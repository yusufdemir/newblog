from django.db import models

# Create your models here.


class UserProfile(models.Model):
    image = models.ImageField(upload_to='photo/', default='photo/None/no-img.jpg')
    phone = models.CharField(max_length=10, blank=True,)
    job = models.CharField(max_length=40, blank=True,)
    validation_key = models.CharField(max_length=24)
    validation = models.BooleanField(default=True)