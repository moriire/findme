from django.db.models.signals import post_save
from django.dispatch import receiver
from bio.models import Bio
#from main.models import Main

@receiver(post_save, sender=Bio)
def update_main(sender, created, instance, **kwargs):
    if created:
        print("Bio created!")
        #main = Main.objects.filter(user = instance.user).first()
        #main.bio = instance
        #main.save()
    return instance