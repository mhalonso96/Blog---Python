from typing import Any

from blog.models.post_models import Post
from blog.views.index_views import PostListView
from django import http
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

PER_PAGE = 9

class CreatedByListView(PostListView):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._temp_context: dict[str, Any] = {}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self._temp_context['user']
        user_full_name = user.username
        if (user.first_name):
            user_full_name = f'{user.first_name} {user.last_name}'
        page_title = user_full_name + ' posts - '
        ctx.update({
            'page_title': page_title
        })
        return ctx
    
    def get_queryset(self) -> QuerySet[Any]:
        qs= super().get_queryset()
        qs = qs.filter(created_by__pk=self._temp_context['user'].pk)
        return qs
        
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        author_pk = self.kwargs.get('author_pk')
        user = User.objects.filter(pk=author_pk).first()

        if user is None:
            raise Http404()
        
        self._temp_context.update({
            'author_pk': author_pk,
            'user': user,
        })

        return super().get(request, *args, **kwargs)
