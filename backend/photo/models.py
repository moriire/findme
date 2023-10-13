from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Photo(models.Model):
    user = models.ForeignKey(User, related_name="user_photo", on_delete=models.CASCADE)
    img = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}-{self.created_on}"