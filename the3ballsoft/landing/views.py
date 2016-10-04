# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re
from django.shortcuts import render
from django.views.generic import View

from users.models import User
from .models import Content



class HomeView(View):
    template_name='pages/home.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['content'] = Content.objects.all()

        return render(request, self.template_name, ctx)


# class ProjectView(View):
    # template_name='pages/project_detail.html'

    # def get(self, request, slug, *args, **kwargs):
        # ctx = self.get_context_data(**kwargs)
        # ctx['project'] = Project.objects.all()
        # return render(request, self.template_name, ctx)





