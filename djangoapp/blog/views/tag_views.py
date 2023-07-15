from blog.views import PostListView

PER_PAGE = 9

class TagListView(PostListView):
    allow_empty= False

    def get_queryset(self) :
        return super().get_queryset().filter(tags__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        page_title = (f'{self.object_list[0].tags.first().name} - Tag - ') #type: ignore
        ctx.update({
            'page_title': page_title
        })
        return ctx