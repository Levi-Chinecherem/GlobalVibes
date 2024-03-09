# community/urls.py
from django.urls import path
from .views import community_list, community_chat, send_chat

urlpatterns = [
    path('', community_list, name='community_list'),
    path('<int:community_id>/chat/', community_chat, name='community_chat'),
    path('<int:community_id>/send_chat/', send_chat, name='send_chat'),
]
