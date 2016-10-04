# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from ckeditor.fields import RichTextField


class Content(models.Model):
    code = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    content_es = RichTextField()
    content_en = RichTextField()

    def __str__(self):
        return self.code
