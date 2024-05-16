from django.db import models

from cloudinary.models import CloudinaryField
from users.models import UserProfile

class UserMessage(models.Model):
     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
     reciever = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reciever')
     msg_content = models.TextField()
     puzzle_photo = CloudinaryField('image', default='placeholder')
     created_at = models.DateTimeField(auto_now=True)
