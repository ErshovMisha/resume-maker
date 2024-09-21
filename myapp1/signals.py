from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Res_Input

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Res_Input.objects.create(user=instance)
