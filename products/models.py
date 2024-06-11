from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import UserProfile

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
  category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
  sku = models.CharField(max_length=254, null=True, blank=True)
  name = models.CharField(max_length=254)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
  image = CloudinaryField('image', default='placeholder')

  def __str__(self):
        return self.name

class Reviews(models.Model):
    """Creates a model for the comments on recipe posts"""

    product = models.ForeignKey(
    Product, on_delete=models.CASCADE, related_name="review"
    )
    author = models.ForeignKey(
    UserProfile, on_delete=models.CASCADE, related_name="reviewer"
    )
    review_body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"Review of {self.product.name} by {self.author}"