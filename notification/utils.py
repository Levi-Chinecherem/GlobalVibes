# notification/utils.py
from .models import Notification

def create_notification(user, action, link=None, target=None, notification_type=None, blog=None, **kwargs):
    """
    Create a new notification for the user.
    Returns True on success, False on failure.
    """
    try:
        Notification.objects.create(user=user, action=action, link=link)
        return True
    except Exception as e:
        print(f"Error creating notification: {e}")
        return False

def mark_notification_as_viewed(notification_id):
    """
    Mark a notification as viewed.
    Returns True on success, False on failure.
    """
    try:
        notification = Notification.objects.get(pk=notification_id)
        notification.viewed = True
        notification.save()
        return True
    except Exception as e:
        print(f"Error marking notification as viewed: {e}")
        return False

def get_unread_notifications_count(user):
    """
    Get the count of unread notifications for the user.
    Returns the count on success, -1 on failure.
    """
    try:
        return Notification.objects.filter(user=user, viewed=False).count()
    except Exception as e:
        print(f"Error getting unread notifications count: {e}")
        return -1

# Add the missing function below
def get_unread_notifications(user):
    """
    Get the unread notifications for the user.
    Returns a queryset of unread notifications on success, an empty queryset on failure.
    """
    try:
        return Notification.objects.filter(user=user, viewed=False)
    except Exception as e:
        print(f"Error getting unread notifications: {e}")
        return Notification.objects.none()
