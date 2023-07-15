from typing import Any

from blog.models.post_models import Post
from blog.views.index_views import PostListView
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render

PER_PAGE = 9

class CategoryListView(PostListView):
    allow_empty= False

    def get_queryset(self) :
        return super().get_queryset().filter(category__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        page_title = (f'{self.object_list[0].category.name} - Categoria - ') #type: ignore
        ctx.update({
            'page_title': page_title
        })
        return ctx

