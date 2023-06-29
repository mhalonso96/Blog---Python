from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

PER_PAGE = 9

def search (request):
    search_value = request.GET.get('search', '').strip()
    posts =Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value) 
        )[0:PER_PAGE]
    
    page_title = f'{search_value[:30]} - Search - '
    
    return render(
        
        request,
        'blog/pages/index.html',{
            'page_obj': posts,
            'search_value': search_value,
            'page_title' : page_title,
        }     
    )

