# blog/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField  # Assuming you're using CKEditor for content
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Category Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tag Title")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Blog Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    cover_image = models.ImageField(upload_to="blog_covers/", verbose_name="Cover Image")
    content = RichTextUploadingField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    tags = models.ManyToManyField(Tag, verbose_name="Tags")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title

class Comment(models.Model):
    source = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Source User")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog")
    commentary = models.TextField(verbose_name="Commentary")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.source.username} - {self.blog.title}"

class Like(models.Model):
    source = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Source User")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Blog")
    like = models.BooleanField(default=True, verbose_name="Like")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return f"{self.source.username} - {self.blog.title}"

