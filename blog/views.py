from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def published_posts(request):
    posts = Post.objects.filter(status="published").order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.view_count += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})