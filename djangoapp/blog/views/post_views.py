from django.shortcuts import render


def post (request):
    return render(
        request,
        'blog/pages/post.html'
    )

