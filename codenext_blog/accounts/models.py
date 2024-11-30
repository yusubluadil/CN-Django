from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

    bio = models.TextField(null=True, blank=True)
    phone_num = models.CharField(max_length=20, null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='media', null=True, blank=True)
