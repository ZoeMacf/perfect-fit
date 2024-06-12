from django.db import models

from cloudinary.models import CloudinaryField
from users.models import UserProfile

class UserMessage(models.Model):
     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
     reciever = models.ManyToManyField(UserProfile, related_name='reciever')
     msg_content = models.TextField()
     created_at = models.DateTimeField(auto_now=True)
