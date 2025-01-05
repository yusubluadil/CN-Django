from rest_framework import serializers

from accounts.api.serializers import (
    CitySerializer,
    UserSerializer
)

from cars.models import (
    Announcement,
    FavoriteAnnouncement,
    AnnouncementImage,
    Brand,
    CarModel,
    RoofType,
    Color,
    CarModel,
    FuelType,
    EngineCapacity,
    ForCountry,
    CarSupply,
    Gearbox
)


class AnnouncementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementImage
        fields = ('image',)


class ListBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class ListRoofTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoofType
        fields = '__all__'


class ListColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ListFuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'


class ListEngineCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineCapacity
        fields = '__all__'


class ListForCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForCountry
        fields = '__all__'


class ListCarSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSupply
        fields = '__all__'


class ListGearboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gearbox
        fields = '__all__'


class CreateAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('user', 'car_supply', 'created_at', 'updated_at', 'is_vip', 'number_of_views')


class ListAnnouncementSerializer(serializers.ModelSerializer):
    frontal_image = serializers.SerializerMethodField()
    brand = ListBrandSerializer(read_only=True)
    car_model = ListModelSerializer(read_only=True)
    engine_capacity = ListEngineCapacitySerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = (
            'id', 'price', 'currency_type', 'brand', 'car_model',
            'released_date', 'engine_capacity', 'mileage', 'mileage_type',
            'city', 'created_at', 'frontal_image'
        )

    def get_frontal_image(self, obj):
        frontal_image_obj = obj.announcement_images.first()
        req = self.context['request']

        try:
            return req.build_absolute_uri(frontal_image_obj.image.url)
        except:
            return None


class DetailAnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    brand = ListBrandSerializer(read_only=True)
    car_model = ListModelSerializer(read_only=True)
    roof_type = ListRoofTypeSerializer(read_only=True)
    color = ListColorSerializer(read_only=True)
    fuel_type = ListFuelTypeSerializer(read_only=True)
    engine_capacity = ListEngineCapacitySerializer(read_only=True)
    for_country = ListForCountrySerializer(read_only=True)
    gearbox = ListGearboxSerializer(read_only=True)

    car_supply = ListCarSupplySerializer(read_only=True, many=True)
    announcement_images = AnnouncementImageSerializer(read_only=True, many=True)

    number_of_views = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = '__all__'

    def get_number_of_views(self, obj):
        obj.number_of_views += 1
        obj.save()

        return obj.number_of_views


class CreateFavoriteAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAnnouncement
        fields = ('announcement',)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ListFavoriteAnnouncementSerializer(serializers.ModelSerializer):
    announcement = ListAnnouncementSerializer()

    class Meta:
        model = FavoriteAnnouncement
        fields = ('announcement',)
