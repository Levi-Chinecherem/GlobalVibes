# notification/admin.py
from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'viewed', 'created_at')
    list_filter = ('viewed', 'created_at')
    search_fields = ('user__username', 'action', 'link')  # Assuming user has a username field

    def user_display(self, obj):
        return obj.user.username

    user_display.short_description = 'User'

admin.site.register(Notification, NotificationAdmin)
