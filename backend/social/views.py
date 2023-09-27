from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Social, SocialSerializer
class SocialView(ModelViewSet):
    queryset = Social.objects.select_related("bio", "social", "user").all()
    serializer_class = SocialSerializer