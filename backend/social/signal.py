from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import User 
from .models import Social
#from main.models import Main

@receiver(post_save, sender=User)
def create_social(sender, created, instance, **kwargs):
    if created:
        print("social created!")
        #social = Social.objects.filter(user = instance.user).first()
        social = Social(user = instance)
        #main.social.add(instance)
        social.save()
    return instance