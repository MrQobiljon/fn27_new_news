from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Post, Category

# Create your views here.


def index(request: WSGIRequest):
    posts = Post.objects.filter(published=True)
    context = {
        "posts": posts,
        "title": "Barcha maqolalar"
    }
    return render(request, "index.html", context)


def posts_by_category(request, category_id):
    posts = get_list_or_404(Post, category_id=category_id, published=True)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        "title": f"{category.name}: barcha maqolalar!"
    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id, published=True)
    post.views += 1
    post.save()

    context = {
        "post": post,
        "title": post.title
    }
    return render(request, 'detail.html', context)







# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(pk=post_id, published=True)
#         post.views += 1
#         post.save()
#
#         context = {
#             "post": post,
#             "title": post.title
#         }
#         return render(request, 'detail.html', context)
#     except:
#         return render(request, "404.html", status=404)