from blog.models.post_models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

PER_PAGE = 9

def created_by (request, id):
    user = User.objects.filter(pk=id).first()
    if user is None:
        raise Http404()
    
    posts =Post.objects.get_published().filter(created_by__pk=id)
    user_full_name = user.username

    if(user.first_name):
        user_full_name = f'{user.first_name} {user.last_name}'
        
    page_title = user_full_name + ' posts - '
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title' : page_title,
        }
    )

