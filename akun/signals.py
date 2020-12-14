from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profil

@receiver(post_save, sender=User)
def buat_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(pengguna=instance)

@receiver(post_save, sender=User)
def simpan_profil(sender, instance, **kwargs):
    instance.profil.save()
