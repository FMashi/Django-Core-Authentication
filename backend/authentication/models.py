
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import os
from django.db import models
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.db.models.signals import post_save
from django.utils import timezone
from .manager import CustomUserManager

import logging
logger = logging.getLogger(__name__)

@deconstructible
class PathRename(object):
    def __init__(self, sub_path):
        self.path = sub_path
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255,verbose_name="Email")
    username = models.CharField(max_length=30, unique=True) 
    first_name = models.CharField(max_length=100, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Last Name")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="Date Joined")
    last_login = models.DateTimeField(default=timezone.now, verbose_name="Last Login")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    is_staff = models.BooleanField(default=False, verbose_name="Staff")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

