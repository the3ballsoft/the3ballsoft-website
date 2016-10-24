# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.template.defaultfilters import truncatechars

from django import forms
from django.contrib import admin
from .models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('code', 'type', 'content_es_short', 'content_en_short')
    search_fields = ['code', 'type']
    list_filter = ('type',)

    def content_es_short(self, obj):
        if obj.type == 'text':
            return truncatechars(obj.content_es, 80)
        else:
            return '<html>'
    content_es_short.short_description = 'content es'

    def content_en_short(self, obj):
        if obj.type == 'text':
            return truncatechars(obj.content_en, 80)
        else:
            return '<html>'
    content_en_short.short_description = 'content en'
