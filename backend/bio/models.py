from django.db import models
class Bio(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_on}"
    
from rest_framework.serializers import ModelSerializer
class BioSerializer(ModelSerializer):
    class Meta:
        model = Bio
        fields = "__all__"