from django.urls import path
from blogs import views as blog_views


urlpatterns = [
    path('', blog_views.ListBlogView.as_view(), name='all_blogs'), # 127.0.0.1:8000/blogs/
    path('create/', blog_views.CreateBlogView.as_view(), name='create_blog'), # 127.0.0.1:8000/blogs/create/
    path('detail/<int:pk>/', blog_views.DetailBlogView.as_view(), name='detail_blog'), # 127.0.0.1:8000/blogs/detail/5/
    path('update/<int:pk>/', blog_views.UpdateBlogView.as_view(), name='update_blog'), # 127.0.0.1:8000/blogs/update/5/
    path('delete/<int:pk>/', blog_views.DeleteBlogView.as_view(), name='delete_blog'), # 127.0.0.1:8000/blogs/delete/5/
]
