from rest_framework import serializers

from ..models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # fields = '__all__' # Blog modelinin bütün fieldləri
        # fields = ('id', 'title') # Blog modelinin göstərilmiş fieldləri
        exclude = ('title', 'about') # Blog modelindən xaric olunmalı fieldlər


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'about')


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
