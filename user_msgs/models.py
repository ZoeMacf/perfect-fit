from django.db import models

from cloudinary.models import CloudinaryField
from users.models import UserProfile

class UserMessage(models.Model):
     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
     message_receiver = models.ManyToManyField(UserProfile, related_name='message_receiver', null=True)
     msg_content = models.TextField()
     created_at = models.DateTimeField(auto_now=True)

     def __str__(self):
        return f"Message from {self.sender}"
