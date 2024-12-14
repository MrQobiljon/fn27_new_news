from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Post, Category

# Create your views here.


def index(request: WSGIRequest):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    context = {
        "posts": posts,
        'categories': categories
    }
    return render(request, "index.html", context)


def posts_by_category(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category_id=category_id, published=True)

    context = {
        "categories": categories,
        'posts': posts
    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id, published=True)

    post.views += 1
    post.save()

    context = {
        "post": post
    }
    return render(request, 'detail.html', context)