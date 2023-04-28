from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User
from utils.logging import CustomLogger

logger = CustomLogger(file_name="exception")


@receiver(post_save, sender=User)
def update_user(instance, created, **kwargs):
    if created:
        user = User.objects.get(instance.id)
        if not user:
            logger.error(f"Can't find the created user. Instance: {str(instance)}")
        user.is_active = True
        user.is_staff = True
        user.save()
