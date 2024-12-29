from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator
)

from . import (
    MILEAGE_CHOICES,
    CURRENCY_CHOICES,
    OWNER_CHOICES,
    TRANSMISSION_CHOICES,
    NUMBER_OF_SEATS_CHOICES
)

from core.utils.models import TrackingModel


USER = get_user_model()


class Brand(models.Model):
    name = models.CharField(max_length=50)


class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=50)


class RoofType(models.Model):
    name = models.CharField(max_length=50)


class Color(models.Model):
    name = models.CharField(max_length=50)


class FuelType(models.Model):
    name = models.CharField(max_length=50)


class EngineCapacity(models.Model):
    volume = models.CharField(max_length=10)


class ForCountry(models.Model):
    name = models.CharField(max_length=50)


class CarSupply(models.Model):
    name = models.CharField(max_length=50)


class Gearbox(models.Model):
    name = models.CharField(max_length=50)


class Announcement(TrackingModel):
    # user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='announcements') # Bəzi hallarda circular import xətası çıxır.
    # user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='announcements')
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='announcements')
    city = models.ForeignKey('accounts.City', on_delete=models.SET_NULL, related_name='announcements', null=True)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='announcements')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='announcements')
    roof_type = models.ForeignKey(RoofType, on_delete=models.CASCADE, related_name='announcements')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='announcements')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='announcements')
    engine_capacity = models.ForeignKey(EngineCapacity, on_delete=models.CASCADE, related_name='announcements')
    for_country = models.ForeignKey(ForCountry, on_delete=models.CASCADE, related_name='announcements')
    gearbox = models.ForeignKey(Gearbox, on_delete=models.CASCADE, related_name='announcements')

    car_supply = models.ManyToManyField(CarSupply, related_name='announcements')

    mileage_type = models.CharField(max_length=5, choices=MILEAGE_CHOICES)
    currency_type = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    owner_type = models.CharField(max_length=10, choices=OWNER_CHOICES)
    transmission_type = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    seat_count = models.CharField(max_length=3, choices=NUMBER_OF_SEATS_CHOICES, null=True, blank=True)

    is_crashed = models.BooleanField(default=False) # Vuruğu var
    is_damaged = models.BooleanField(default=False) # Qəzalı və ya ehtiyat hissələr üçün
    is_colored = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    with_credit = models.BooleanField(default=False)
    barter = models.BooleanField(default=False)

    is_vip = models.BooleanField(default=False)
    is_showroom = models.BooleanField(default=False)

    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    price = models.DecimalField(max_digits=8, decimal_places=0)

    released_date = models.DateField()
    engine_power = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5000)])

    vin_code = models.CharField(max_length=17, validators=[MinLengthValidator(17)])
    info = models.TextField(null=True, blank=True)

    number_of_views = models.IntegerField(default=0)


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='announcement_images')
    image = models.ImageField(upload_to='announcements')
