from django.db import models
from user.models import User
    
class Circle(models.Model):
    user = models.ForeignKey(User, related_name="user_circle", on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    hired = models.ManyToManyField(User, blank=True)
    count = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"
