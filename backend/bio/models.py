from django.db import models
from photo.models import Photo
from django.contrib.auth import get_user_model
User = get_user_model()
class Bio(models.Model):
    user = models.OneToOneField(User, related_name="user_bio", on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(default="")
    images= models.ManyToManyField(Photo, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"
