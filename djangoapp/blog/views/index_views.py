from blog.models.post_models import Post
from django.core.paginator import Paginator
from django.shortcuts import render

posts = list(range(1000))

def index (request): 
    posts = Post.objects.filter(is_published=True).order_by('pk')

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj
        }
    )

