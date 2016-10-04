# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^blog/$', views.LatestView.as_view(), name='home'),
    url(r'^blog/search/$', views.SearchView.as_view(), name='search'),
    url(r'^blog/posts/(?P<slug>[\w-]+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
]
