from django.db import models
from users.models import UserProfile

from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Newsletter(models.Model):
    """Creates a newsletter model"""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="newsletter_posts"
    )
    newsletter_info = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    events_image = CloudinaryField("image", default="placeholder")

    def __str__(self):
        return f"{self.title}"
