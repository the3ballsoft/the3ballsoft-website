# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'user', 'created', 'is_active',)
    search_fields = ('title', 'user__first_name', 'user__last_name', 'subtitle')
    list_filter = ('is_active',)
    ordering = ('-created',)

