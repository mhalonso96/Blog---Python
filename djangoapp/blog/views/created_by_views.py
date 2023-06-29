from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.shortcuts import render

PER_PAGE = 9

def created_by (request, id):
    posts =Post.objects.get_published().filter(created_by__pk=id)
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj
        }
    )
