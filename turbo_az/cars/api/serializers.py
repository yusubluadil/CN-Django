from rest_framework import serializers

from cars.models import (
    Announcement,
    AnnouncementImage,
    Brand
)


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ('image',)


class CreateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('user', 'car_supply', 'created_at', 'updated_at')


class ListBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
