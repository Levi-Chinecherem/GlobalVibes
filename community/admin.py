# community/admin.py

from django.contrib import admin
from .models import Community, Chat

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('user', 'community', 'timestamp')
    search_fields = ('user__username', 'community__title')
    list_filter = ('community',)
    date_hierarchy = 'timestamp'
