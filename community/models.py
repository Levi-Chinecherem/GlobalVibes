# community/models.py

from django.db import models
from accounts.models import CustomUser

class Community(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='community_covers/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'

class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    media_file = models.FileField(upload_to='chat_media/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.community.title} - {self.timestamp}'

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'
