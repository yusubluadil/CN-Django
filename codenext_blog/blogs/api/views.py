from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from ..models import Blog
from .serializers import (
    BlogListSerializer,
    BlogCreateSerializer,
    BlogDetailSerializer
)


@api_view(['GET'])
def all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogListSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_blog(request):
    serializer = BlogCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response({'detail': 'Blog müvəffəqiyyətlə yaradıldı.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def detail_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'GET':
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = BlogDetailSerializer(data=request.data, instance=blog, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog_id = blog.id
        blog.delete()
        return Response({'detail': f'{blog_id} ID-li blog müvəffəqiyyətlə silindi.'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': 'Sorğu növü qəbul edilmir.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)