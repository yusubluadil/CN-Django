from django.urls import path
from blogs import views as blog_views


urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'), # 127.0.0.1:8000/blogs/
    path('create/', blog_views.create_blog, name='create_blog'), # 127.0.0.1:8000/blogs/create/
    path('detail/<int:pk>/', blog_views.detail_blog, name='detail_blog'), # 127.0.0.1:8000/blogs/detail/5/
    path('update/<int:pk>/', blog_views.update_blog, name='update_blog'), # 127.0.0.1:8000/blogs/update/5/
    path('delete/<int:pk>/', blog_views.delete_blog, name='delete_blog'), # 127.0.0.1:8000/blogs/delete/5/
]
