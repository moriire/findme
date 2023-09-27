from django.db.models.signals import post_save
from django.dispatch import receiver
from social.models import Social 
#from main.models import Main

@receiver(post_save, sender=Social)
def update_main(sender, created, instance, **kwargs):
    if created:
        print("social created!")
        #main = Main.objects.filter(user = instance.user).first()
        #main.social.add(instance)
        #main.save()
    return instance