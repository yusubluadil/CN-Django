from django.urls import path, include


urlpatterns = [
    path('blogs/', include('blogs.api.urls')), # 127.0.0.1:8000/api/v1/blogs/...
    # path('accounts/', include('accounts.api.urls')), # 127.0.0.1:8000/api/v1/blogs/...
]
