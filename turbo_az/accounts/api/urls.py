from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.urls import path

from . import views as account_views


urlpatterns = [
    path('register/', account_views.RegisterAPIView.as_view()), # 127.0.0.1:8000/api/v1/accounts/register/
    path('me/', account_views.MeAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

"""
JWT - Json Web Token (https://jwt.io/introduction)

token/ - refresh və access token generate edən hissə
token/refresh/ - verilmiş refresh token əsasında access token yaradan hissə
token/verify/ - daxil edilən tokenlərin valid olub-olmamasını yoxlayan hissə

"""
