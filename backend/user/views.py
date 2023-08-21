from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, UserSerializer
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer