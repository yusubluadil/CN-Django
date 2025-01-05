import django_filters

from accounts.models import City

from .. import TRANSMISSION_CHOICES
from ..models import (
    Announcement,
    RoofType,
    Color,
    FuelType,
    Gearbox,
    CarSupply
)

# exact - Yalnız verilmiş dəyərə uyğun olanları göstər
# icontains - Verilmiş məlumata oxşar olan bütün məlumatları gətir. (Böyük və kiçik hərflərə həssas deyil.)
    # Məsələn, Query olaraq `merc` göndərilibsə, tərkibində `merc` olan bütün məlumatları verəcək.
# lt (less than), gt (greater than) - Uyğun olaraq daxil edilmiş məlumatdan kiçik və böyük olanları verir.
    # creted_at__lt=14-12-2024
# lte (less than or equal), gte (greater than or equal) - Uyğun olaraq daxil edilmiş məlumatdan kiçik və ya bərabər və böyük və ya bərabər olanları verir.
    # creted_at__lte=14-12-2024


# class AnnouncementFilter(django_filters.FilterSet):
#     roof_type = django_filters.ModelMultipleChoiceFilter(queryset=RoofType.objects.all())
#     color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all())
#     fuel_type = django_filters.ModelMultipleChoiceFilter(queryset=FuelType.objects.all())
#     gearbox = django_filters.ModelMultipleChoiceFilter(queryset=Gearbox.objects.all())
#     city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all())

#     class Meta:
#         model = Announcement
#         fields = {
#             'brand': ['exact'],
#             'car_model': ['exact'],
#             'currency_type': ['exact'],
#             'is_new': ['exact'],
#             'price': ['gte', 'lte'],
#             'with_credit': ['exact'],
#             'barter': ['exact'],
#             'released_date': ['gte', 'lte'],
#         }


class AnnouncementFilter(django_filters.FilterSet):
    #IL
    min_year = django_filters.NumberFilter(
        field_name="released_date",
        lookup_expr='year__gte',
        label="Min Year",
    )
    max_year = django_filters.NumberFilter(
        field_name="released_date",
        lookup_expr='year__lte',
        label="Max Year",
    )

    roof_type = django_filters.ModelMultipleChoiceFilter(queryset=RoofType.objects.all())
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all())
    fuel_type = django_filters.ModelMultipleChoiceFilter(queryset=FuelType.objects.all())
    gearbox = django_filters.ModelMultipleChoiceFilter(queryset=Gearbox.objects.all())
    city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all())
    fuel_type = django_filters.ModelMultipleChoiceFilter(queryset=FuelType.objects.all())
    car_supply = django_filters.ModelMultipleChoiceFilter(queryset=CarSupply.objects.all())

    #Ötürücü-ön arxa tam
    transmission_type = django_filters.MultipleChoiceFilter(
        field_name="transmission_type",
        choices=TRANSMISSION_CHOICES
    )

    #Muherrikin gucu
    min_engine_power= django_filters.NumberFilter( 
        field_name='engine_power', 
        lookup_expr='gte'
    )
    max_engine_power= django_filters.NumberFilter( 
        field_name='engine_power', 
        lookup_expr='lte'
    )

    #Yürüş
    min_mileage= django_filters.NumberFilter( 
        field_name='mileage', 
        lookup_expr='gte'
    )
    max_mileage= django_filters.NumberFilter( 
        field_name='mileage', 
        lookup_expr='lte'
    )

    class Meta:
        model = Announcement
        fields = {
            'brand': ['exact'],
            'car_model': ['exact'],
            'currency_type': ['exact'],
            'is_new': ['exact'],
            'price': ['gte', 'lte'],
            'with_credit': ['exact'],
            'barter': ['exact'],
            'engine_capacity':['gte','lte'],#obj kimi gorunur yeniden bax
            'engine_power':['gte','lte'],
            'seat_count': ['exact'],
            'owner_type':['exact'],
            'for_country':['exact'], #obj 
            'is_crashed': ['exact'],
            'is_damaged': ['exact'],
            'is_colored': ['exact'],
            'is_dealer': ['exact'],
    }
