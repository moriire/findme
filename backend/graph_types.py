import graphene
from graphene_django import DjangoObjectType
from bio.models import Bio
from photo.models import Photo
from circle.models import Circle
from social.models import Social
from django.contrib.auth import get_user_model

User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class UploadType(DjangoObjectType):
    class Meta:
        model = Photo
        fields = ("img",)

class CircleType(DjangoObjectType):
    class Meta:
        model = Circle
        fields = "__all__"

class BioType(DjangoObjectType):
    class Meta:
        model = Bio
        fields = (
            "user",
            "body",
            "images"
        )

class SocialType(DjangoObjectType):
    class Meta:
        model = Social
        fields = "__all__"  
