from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Social, SocialSerializer
class SocialView(ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer