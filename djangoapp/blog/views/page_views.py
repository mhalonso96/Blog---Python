from blog.models.page_models import Page
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render


def page (request,slug):
    page_obj = (
        Page.objects
        .filter(is_published=True)
        .filter(slug=slug)
        .first())
    
    if page_obj is None:
        raise Http404()

    page_title = f'{page_obj.title} - Página - '
   
    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_obj,
            'page_title' : page_title,
        }
    )

