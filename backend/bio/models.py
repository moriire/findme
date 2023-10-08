from django.db import models
from user.models import User
    
class Bio(models.Model):
    user = models.OneToOneField(User, related_name="user_bio", on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"
