# notification/models.py
from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Describe the action that triggers the notification
    link = models.CharField(max_length=255)    # Link to the related content
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action}'

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
