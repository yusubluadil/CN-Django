from django.contrib import admin

from blogs.models import Blog, Category


admin.site.register(Blog)
admin.site.register(Category)
