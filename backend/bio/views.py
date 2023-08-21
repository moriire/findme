from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Bio, BioSerializer
class BioView(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer
# Create your views here.
