# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('code', 'type')
