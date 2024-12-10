from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .models import Post, Category

# Create your views here.


def index(request: WSGIRequest):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "index.html", context)