from django.urls import path
from .views import get_notification_count

urlpatterns = [
    path('get_notification_count/', get_notification_count, name='get_notification_count'),
]
