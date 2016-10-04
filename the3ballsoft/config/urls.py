# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django.contrib import admin
from django.views import defaults
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Main
    url('', include('landing.urls', namespace='landing')),
    url('', include('blog.urls', namespace='blog')),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),

    #CKeditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', defaults.bad_request),
        url(r'^403/$', defaults.permission_denied),
        url(r'^404/$', defaults.page_not_found),
        url(r'^500/$', defaults.server_error),
    ]
    # static/media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

