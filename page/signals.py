# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print(f"Signal triggered for user: {instance.username}, created: {created}")
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()