from django.db import models
from rest_framework.serializers import ModelSerializer
from user.models import User
from bio.models import Bio
from social.models import Social
class Main(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="main_user_id")
    bio = models.ForeignKey(Bio, related_name="main_user_bio", on_delete=models.SET_DEFAULT, default="")
    social = models.ManyToManyField(Social, blank=True)


class MainSerializer(ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"
