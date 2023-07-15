from typing import Any

from blog.models.post_models import Post
from blog.views import PostListView
from django import http
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render

PER_PAGE = 9
class SearchListView(PostListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_value = ''
        
    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(
        Q(title__icontains=self._search_value) |
        Q(excerpt__icontains=self._search_value) |
        Q(content__icontains=self._search_value) 
        )[0:PER_PAGE]
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'page_title': f'{self._search_value[:30]} - Search -',
            'search_value': self._search_value
        })
        return ctx
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        if self._search_value == '' :
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)
