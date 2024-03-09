# myapp/admin.py

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_resolved')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_resolved']

    def mark_as_resolved(modeladmin, request, queryset):
        queryset.update(is_resolved=True)
    mark_as_resolved.short_description = "Mark selected messages as resolved"

admin.site.register(Contact, ContactAdmin)
