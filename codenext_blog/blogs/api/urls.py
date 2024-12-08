from django.urls import path
from . import views as blog_views


urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'), # 127.0.0.1:8000/api/v1/blogs/ (endpoint)
    path('create/', blog_views.create_blog, name='create_blog'), # 127.0.0.1:8000/api/v1/blogs/create/ (endpoint)
    path('detail/<int:pk>/', blog_views.detail_blog, name='detail_blog'), # 127.0.0.1:8000/api/v1/blogs/detail/123/ (endpoint)
    path('update/<int:pk>/', blog_views.detail_blog, name='update_blog'), # 127.0.0.1:8000/api/v1/blogs/update/123/ (endpoint)
    path('delete/<int:pk>/', blog_views.detail_blog, name='delete_blog'), # 127.0.0.1:8000/api/v1/blogs/delete/123/ (endpoint)
]
