from django.contrib import admin
from .models import Category, Tag, Blog, Comment, Like
from ckeditor.widgets import CKEditorWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'tags', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('source', 'blog', 'created_at')
    search_fields = ('source__username', 'blog__title', 'commentary')
    date_hierarchy = 'created_at'

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('source', 'blog', 'like', 'created_at')
    search_fields = ('source__username', 'blog__title')
    date_hierarchy = 'created_at'

# @admin.register(CommentReply)
# class CommentReplyAdmin(admin.ModelAdmin):
#     list_display = ('source', 'comment', 'created_at')
#     search_fields = ('source__username', 'comment__commentary', 'reply')
#     date_hierarchy = 'created_at'
