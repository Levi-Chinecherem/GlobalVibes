# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

admin.site.site_title = _('Global Vibes Admin')
admin.site.site_header = _('Global Vibes Administration')
admin.site.index_title = _('globalvibes.net Administration')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'profile_image', 'promoter', 'is_staff']
    search_fields = ['username', 'email']
    list_filter = ['promoter', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Promoter Info', {'fields': ('promoter',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
