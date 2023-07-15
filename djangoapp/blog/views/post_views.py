from blog.models.post_models import Post
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView

PER_PAGE = 9
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        post = self.get_object()
        page_title = f'{post.title} - Post -' #type: ignore
        ctx.update({
            'page_title': page_title
        })
        return ctx
    
    def get_queryset(self):
        return super().get_queryset().filter(is_published= True)


