from .utils import get_unread_notifications_count, get_unread_notifications

def notifications_context(request):
    if request.user.is_authenticated:
        unread_count = get_unread_notifications_count(request.user)
        unread_notifications = get_unread_notifications(request.user)
    else:
        unread_count = 0
        unread_notifications = []

    return {'notification_unread_count': unread_count, 'unread_notifications': unread_notifications}
