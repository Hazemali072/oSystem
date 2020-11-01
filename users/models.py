from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    name = models.CharField(max_length = 255,blank = False ,null = False)
    level = models.IntegerField(blank = True,null = True)
    notifications = models.BooleanField(default=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','level']

    objects = CustomUserManager()

    def __str__(self):
        return self.email