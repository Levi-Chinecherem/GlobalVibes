# blog/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.utils import create_notification
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog, Comment
from accounts.models import CustomUser

@receiver(post_save, sender=Blog)
def create_blog_notification(sender, instance, created, **kwargs):
    if created:
        all_users = CustomUser.objects.all()
        for user in all_users:
            create_notification(
                user=user,
                action='New blog created',
                link=f'/blog/{instance.pk}/',  # Provide the appropriate link for the notification
            )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        create_notification(
            user=instance.blog.author,
            action='New comment on your blog',
            target=instance.source,  # Update here to use the comment source as the target
            link=f'/blog/{instance.blog.pk}/#comment-{instance.pk}',
        )
