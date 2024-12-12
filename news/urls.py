from django.urls import path

from .views import index, posts_by_category, post_detail

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
]

