from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Main, MainSerializer

class MainView(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer