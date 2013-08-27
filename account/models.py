from AptUrl.Helpers import _
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    # user
    user = models.OneToOneField(User)

    # activate True False
    activate = models.BooleanField(default=False)

    # activation key
    activation_key = models.CharField(max_length=30, null=True)

    # gender
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              null=True,
                              blank=True)


    # user profile photo
    image = models.ImageField(_("Profile Pic"),
                              upload_to="photo/",
                              null=True,
                              blank=True
                              )

    def __unicode__(self):
        return "%s Details" % self.email

    def activate(self):  #activate user
        self.activate = True
        self.save()
        return self.activate


def create_user_profile(sender, instance, created, **kwargs):
    """
    import ipdb
    ipdb.set_trace()
    n = next
    c = contnio
    """
    if created:
        created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)