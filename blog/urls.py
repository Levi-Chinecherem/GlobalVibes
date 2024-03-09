
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', v.blog_detail, name='blog_detail'),
    path('like/', v.like_blog, name='like_blog'),
]
