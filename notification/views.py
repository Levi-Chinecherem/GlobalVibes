# notification/views.py
from django.shortcuts import render, get_object_or_404
from .models import Notification
from .utils import get_unread_notifications_count, get_unread_notifications
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required

def notification_list(request):
    """
    Display the list of notifications for the user.
    """
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    unread_count = get_unread_notifications_count(request.user)

    return render(request, 'notification/notification_list.html', {'notifications': notifications, 'unread_count': unread_count})
 
@login_required
def get_notification_count(request):
    if request.user.is_authenticated:
        # Mark viewed notifications
        Notification.objects.filter(user=request.user, viewed=False).update(viewed=True)

        # Retrieve the remaining unread notifications
        unread_notifications = Notification.objects.filter(user=request.user, viewed=False)[:5]
        unread_count = unread_notifications.count()

        # Serialize notifications if needed
        serialized_notifications = [{'message': notification.message, 'link': notification.link} for notification in unread_notifications]

        return JsonResponse({'notification_unread_count': unread_count, 'notifications': serialized_notifications})
    else:
        return JsonResponse({'notification_unread_count': 0, 'notifications': []})