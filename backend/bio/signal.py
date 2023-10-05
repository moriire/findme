from django.db.models.signals import post_save
from django.dispatch import receiver
from bio.models import Bio
from user.models import User
#from main.models import Main
@receiver(post_save, sender=User)
def create_user_bio(sender, instance, created, **kwargs):
    if created:
        bio = Bio.objects.create(user=instance)
        bio.save()
"""
@receiver(post_save, sender=User)
def save_user_bio(sender, instance, **kwargs):
    Bio()
    instance.bio.save()
"""