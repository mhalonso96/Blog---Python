from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

PER_PAGE = 9

def post (request, slug):
    post_obj = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
        )
    
    if post_obj is None:
        raise Http404()

    page_title = f'{post_obj.title} - Post - '
    

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post_obj,
            'page_title' : page_title,
        }
    )

