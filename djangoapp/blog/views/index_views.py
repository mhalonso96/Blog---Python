from typing import Any, Dict

from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

PER_PAGE = 9

class PostListView(ListView):
    template_name = 'blog/pages/index.html'
    context_object_name = 'posts'
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published= True)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Home -'
        })
        return context
    