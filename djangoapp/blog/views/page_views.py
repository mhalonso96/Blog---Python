from typing import Any, Dict

from blog.models.page_models import Page
from django.db import models
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView


class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field =  'slug'
    context_object_name = 'page'
    
    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        page = self.get_object()
        page_title = f'{page.title} - Página -' #type: ignore
        ctx.update({
            'page_title': page_title
        })
        return ctx
    
    def get_queryset(self):
        return super().get_queryset().filter(is_published= True)


