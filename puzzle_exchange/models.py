from django.db import models
from users.models import UserProfile
from cloudinary.models import CloudinaryField

class PuzzleExchange(models.Model):

 submission_title = models.CharField(max_length=200, unique=True)
 poster = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='puzzle_submission')
 submitted_on = models.DateTimeField(auto_now=True)
 approved_submission = models.BooleanField(default=False)
 submission_text = models.TextField()
 puzzle_image = CloudinaryField("image", default="placeholder")

 def __str__(self):
          return f"{self.submission_title}"
