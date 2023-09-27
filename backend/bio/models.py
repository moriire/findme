from django.db import models
from user.models import User
from rest_framework.serializers import ModelSerializer
class Bio(models.Model):
    user = models.ForeignKey(User, related_name="user_bio", on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_on}"

class BioSerializer(ModelSerializer):
    class Meta:
        model = Bio
        fields = "__all__"