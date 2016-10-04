# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField
from users.models import User


class Article(models.Model):
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='title', unique=True)
    subtitle = models.CharField(max_length=500, blank=True)
    photo = VersatileImageField(upload_to='img/articles')
    content = RichTextField()
    user = models.ForeignKey(User, related_name='articles')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    modified = models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')

    def __str__(self):
        return self.slug
