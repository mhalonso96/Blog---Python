from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.shortcuts import render


def page (request,slug):
   
    return render(
        request,
        'blog/pages/page.html',
        {
            #'page_obj': page_obj
        }
    )

