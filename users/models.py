from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=20, null=True, blank=True)
  user_image = CloudinaryField("image", default="placeholder")
  user_phone_number = models.CharField(max_length=20, null=True, blank=True)
  user_street_address1 = models.CharField(max_length=80, null=True, blank=True)
  user_street_address2 = models.CharField(max_length=80, null=True, blank=True)
  user_town_or_city = models.CharField(max_length=40, null=True, blank=True)
  user_county = models.CharField(max_length=80, null=True, blank=True)
  user_postcode = models.CharField(max_length=20, null=True, blank=True)
  user_country = CountryField(blank_label='Country', null=True, blank=True)

  def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
  """
  Create or update a user profile
  """
  if created: 
    UserProfile.objects.create(user=instance)
  # Existing users: just save the profile
  instance.userprofile.save()
