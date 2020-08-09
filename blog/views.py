from django.shortcuts import render, get_object_or_404

from .models import Post


def allblogs(request):
    blog = Post.objects
    return render(request, 'blog/allblogs.html', {'blog': blog})


def detail(request, blog_id):
    detailblog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
