from django.db import models
from django.contrib.auth.models import UserProfile
from django.db.models import Avg


class Review(models.Model):
    review_title = models.CharField(max_length=100, default="Header")
    review_content = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Review, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"