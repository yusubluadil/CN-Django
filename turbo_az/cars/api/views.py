from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cars.models import (
    Announcement,
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

from .serializers import (
    CreateAnnouncementSerializer,
    ListBrandSerializer,
    ListModelSerializer,
    ListRoofTypeSerializer,
    ListColorSerializer,
    ListFuelTypeSerializer,
    ListEngineCapacitySerializer,
    ListForCountrySerializer,
    ListCarSupplySerializer,
    ListGearboxSerializer
    
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
