from django.urls import path, include


urlpatterns = [
    path('cars/', include('cars.api.urls'))
]