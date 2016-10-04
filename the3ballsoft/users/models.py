# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from versatileimagefield.fields import VersatileImageField


@python_2_unicode_compatible
class User(AbstractUser):
    avatar = VersatileImageField(
        upload_to='img/avatars',
        max_length=500,
        null=True,
        blank=True
    )
    caption = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

