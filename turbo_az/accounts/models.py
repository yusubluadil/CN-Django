from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class City(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ('name',)


class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=16, unique=True, blank=True) # +994 70 919 2969

    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='users', null=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone_number
