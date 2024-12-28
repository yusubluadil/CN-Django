from rest_framework import (
    generics,
    status
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    RegisterSerializer,
    MeSerializer
)

from ..models import User


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MeAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = MeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
