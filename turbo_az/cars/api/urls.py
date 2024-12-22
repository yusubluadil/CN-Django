from django.urls import path

from . import views as cars_views


urlpatterns = [
    path('create/', cars_views.CreateAnnouncementAPIView.as_view()),
    path('brands/', cars_views.ListBrandAPIView.as_view()),
]