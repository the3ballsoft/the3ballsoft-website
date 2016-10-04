# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^projects/(?P<slug>[\w-]+)/$', views.ProjectView.as_view(), name='projects'),
]
