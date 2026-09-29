from django.urls import path

from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('published/', views.published_posts, name='published_posts'),
]