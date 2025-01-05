from django.urls import path

from . import views as cars_views


urlpatterns = [
    path('create/', cars_views.CreateAnnouncementAPIView.as_view()), # endpoint
    path('announcements/', cars_views.ListAnnouncementAPIView.as_view()),
    path('announcements/<int:pk>/', cars_views.DetailAnnouncementAPIView.as_view()),

    path('create-favorite-announcements/', cars_views.CreateFavoriteAnnouncementAPIView.as_view()),
    path('favorite-announcements/', cars_views.ListFavoriteAnnouncementAPIView.as_view()),

    path('brands/', cars_views.ListBrandAPIView.as_view()),
    path('models/', cars_views.ListModelAPIView.as_view()),
    path('roof-types/', cars_views.ListRoofTypeAPIView.as_view()),
    path('colors/', cars_views.ListColorAPIView.as_view()),
    path('fuel-types/', cars_views.ListFuelTypeAPIView.as_view()),
    path('engine-capacities/', cars_views.ListEngineCapacityAPIView.as_view()),
    path('for-countries/', cars_views.ListForCountryAPIView.as_view()),
    path('car-supplies/', cars_views.ListCarSupplyAPIView.as_view()),
    path('gearboxes/', cars_views.ListGearboxAPIView.as_view()),
]
