from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.shortcuts import render

PER_PAGE = 9

def post (request, slug):
    post = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
        ) 

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post
        }
    )

