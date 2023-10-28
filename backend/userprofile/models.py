import os
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from authentication.models import CustomUser

@deconstructible
class PathRename(object):
    def __init__(self, sub_path):
        self.path = sub_path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)


class Profile(models.Model):
    GENDERS = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    phone = models.CharField(max_length=15, blank=True, null=True)
    bio = models.CharField(max_length=100,blank=True)
    image = models.ImageField(default='person.png', upload_to=PathRename('images/profile'))
    gender = models.CharField(max_length=255, blank=True, null=True, choices=GENDERS)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{} Profile.'.format(self.user.first_name)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(save_user_profile, sender=CustomUser)