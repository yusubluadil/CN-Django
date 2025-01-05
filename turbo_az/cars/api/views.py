from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

from .filters import AnnouncementFilter
from .serializers import (
    CreateAnnouncementSerializer,
    CreateFavoriteAnnouncementSerializer,
    ListFavoriteAnnouncementSerializer,
    ListBrandSerializer,
    ListModelSerializer,
    ListRoofTypeSerializer,
    ListColorSerializer,
    ListFuelTypeSerializer,
    ListEngineCapacitySerializer,
    ListForCountrySerializer,
    ListCarSupplySerializer,
    ListGearboxSerializer,
    ListAnnouncementSerializer,
    DetailAnnouncementSerializer
)
from .services.announcement_service import create_announcement


class CreateAnnouncementAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = CreateAnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.headers)
        user = request.user
        images = request.FILES.getlist('images')
        car_supply = [int(i) for i in request.data.pop('car_supply')[0].split(',')]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = create_announcement(user=user, car_supply=car_supply, **serializer.validated_data)

        for image in images:
            AnnouncementImage.objects.create(announcement_id=obj.id, image=image)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListAnnouncementAPIView(generics.ListAPIView):
    queryset = Announcement.objects.select_related('brand', 'car_model', 'engine_capacity', 'city')
    serializer_class = ListAnnouncementSerializer
    filterset_class = AnnouncementFilter


class DetailAnnouncementAPIView(generics.RetrieveAPIView):
    queryset = Announcement.objects.select_related(
        'brand', 'car_model', 'roof_type', 'color', 'fuel_type', 'engine_capacity',
        'for_country', 'gearbox', 'city', 'user'
    ).prefetch_related(
        'car_supply'
    )
    serializer_class = DetailAnnouncementSerializer

    def get(self, request, *args, **kwargs):
        print(id(request.user))
        return super().get(request, *args, **kwargs)


class ListBrandAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = ListBrandSerializer


class ListModelAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = ListModelSerializer


class ListRoofTypeAPIView(generics.ListAPIView):
    queryset = RoofType.objects.all()
    serializer_class = ListRoofTypeSerializer


class ListColorAPIView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ListColorSerializer


class ListFuelTypeAPIView(generics.ListAPIView):
    queryset = FuelType.objects.all()
    serializer_class = ListFuelTypeSerializer


class ListEngineCapacityAPIView(generics.ListAPIView):
    queryset = EngineCapacity.objects.all()
    serializer_class = ListEngineCapacitySerializer


class ListForCountryAPIView(generics.ListAPIView):
    queryset = ForCountry.objects.all()
    serializer_class = ListForCountrySerializer


class ListCarSupplyAPIView(generics.ListAPIView):
    queryset = CarSupply.objects.all()
    serializer_class = ListCarSupplySerializer


class ListGearboxAPIView(generics.ListAPIView):
    queryset = Gearbox.objects.all()
    serializer_class = ListGearboxSerializer


class CreateFavoriteAnnouncementAPIView(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = CreateFavoriteAnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListFavoriteAnnouncementAPIView(generics.ListAPIView):
    serializer_class = ListFavoriteAnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.request.user.favorite_announcements.select_related('announcement')
        return queryset