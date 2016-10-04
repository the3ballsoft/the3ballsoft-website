# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re
import datetime
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from users.models import User
from .models import Article


class LatestView(View):
    template_name='pages/blog_latest.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        articles = Article.objects.order_by('-created')[100]

        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        try:
            query = paginator.page(page)
        except PageNotAnInteger:
            query = paginator.page(1)
        except EmptyPage:
            query = paginator.page(paginator.num_pages)

        ctx['articles'] = query
        return render(request, self.template_name, ctx)


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields. '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

class SearchView(View):
    template_name='pages/blog_search.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        entry_query = get_query(request.GET.get('q'), ['title', 'subtitle', 'content'])
        articles = Article.objects.filter(entry_query).order_by('-created')[:200]

        paginator = Paginator(articles, 10)
        page = request.GET.get('page')
        try:
            query = paginator.page(page)
        except PageNotAnInteger:
            query = paginator.page(1)
        except EmptyPage:
            query = paginator.page(paginator.num_pages)

        ctx['results'] = query
        return render(request, self.template_name, ctx)

class ArticleDetailView(View):
    template_name='pages/blog_article_detail.html'

    def get(self, request, slug, *args, **kwargs):
        ctx = {}
        ctx['article'] = Article.objects.select_related('user').get(slug=slug)
        return render(request, self.template_name, ctx)


