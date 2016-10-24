# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from users.models import User
from .models import Content



class HomeView(View):
    template_name='pages/home.html'


    def get(self, request, *args, **kwargs):
        ctx = {}
        obj = list(Content.objects.all())
        types = []

        # send content depending lenguage
        def trans(ele):
            return ele.content_es if settings.LANGUAGE_CODE == 'es-CO' else ele.content_en

        # bind text directly or group by type
        for ele in obj:
            if ele.type == 'text' or ele.type == 'html':
                ctx[ele.code] = trans(ele)
            else:
                if ele.type not in types:
                    ctx[ele.type] = []
                    types.append(ele.type)

                ctx[ele.type].append(trans(ele))


        # print(ctx)

        return render(request, self.template_name, ctx)



# class ProjectView(View):
    # template_name='pages/project_detail.html'

    # def get(self, request, slug, *args, **kwargs):
        # ctx = self.get_context_data(**kwargs)
        # ctx['project'] = Project.objects.all()
        # return render(request, self.template_name, ctx)
