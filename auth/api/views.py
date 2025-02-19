from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer
from rest_framework.response import Response

# Регистрация пользователя
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Получение информации о текущем пользователе
class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({"id": user.id, "username": user.username, "email": user.email})

