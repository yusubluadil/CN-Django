from django.contrib import admin

from .models import (
    Brand,
    CarModel,
    RoofType,
    Color,
    FuelType,
    EngineCapacity,
    ForCountry,
    CarSupply,
    Gearbox,
    Announcement,
    AnnouncementImage,
)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name')
    list_filter = ('brand',)
    search_fields = ('name',)
    list_per_page = 25


@admin.register(RoofType)
class RoofTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(EngineCapacity)
class EngineCapacityAdmin(admin.ModelAdmin):
    list_display = ('id', 'volume')
    list_per_page = 25


@admin.register(ForCountry)
class ForCountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(CarSupply)
class CarSupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(Gearbox)
class GearboxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


@admin.register(AnnouncementImage)
class AnnouncementImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement')
    list_filter = ('announcement',)
    list_per_page = 25


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    # search_fields = ('name',)
    list_per_page = 25
