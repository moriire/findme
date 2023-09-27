from django.db import models
from graphene_django import DjangoObjectType
from user.models import User
class Social(models.Model):
    SOCIAL = (
        ("facebook", "facebook"),
        ("linkedin", "linkedin"),
        ("instagram", "instagram"),
        ("twitter", "twitter")
    )
    user = models.ForeignKey(User, related_name="user_social", on_delete=models.CASCADE)
    name = models.CharField(max_length=12, choices=SOCIAL)
    url = models.URLField()
    def __str__(self) -> str:
        return self.url

from rest_framework.serializers import ModelSerializer
class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"