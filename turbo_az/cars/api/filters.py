import django_filters

from accounts.models import City

from ..models import (
    Announcement,
    RoofType,
    Color,
    FuelType,
    Gearbox
)

# exact - Yalnız verilmiş dəyərə uyğun olanları göstər
# icontains - Verilmiş məlumata oxşar olan bütün məlumatları gətir. (Böyük və kiçik hərflərə həssas deyil.)
    # Məsələn, Query olaraq `merc` göndərilibsə, tərkibində `merc` olan bütün məlumatları verəcək.
# lt (less than), gt (greater than) - Uyğun olaraq daxil edilmiş məlumatdan kiçik və böyük olanları verir.
    # creted_at__lt=14-12-2024
# lte (less than or equal), gte (greater than or equal) - Uyğun olaraq daxil edilmiş məlumatdan kiçik və ya bərabər və böyük və ya bərabər olanları verir.
    # creted_at__lte=14-12-2024


class AnnouncementFilter(django_filters.FilterSet):
    roof_type = django_filters.ModelMultipleChoiceFilter(queryset=RoofType.objects.all())
    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all())
    fuel_type = django_filters.ModelMultipleChoiceFilter(queryset=FuelType.objects.all())
    gearbox = django_filters.ModelMultipleChoiceFilter(queryset=Gearbox.objects.all())
    city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all())

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
            'released_date': ['gte', 'lte'],
        }
