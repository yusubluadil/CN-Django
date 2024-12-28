from django.urls import path, include


urlpatterns = [
    path('cars/', include('cars.api.urls')),
    path('accounts/', include('accounts.api.urls')),
]