from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Leeds, CheckPhone

@receiver(post_save, sender=Leeds)
def create_book_for_author(sender, instance, created, **kwargs):
    if created:
        CheckPhone.objects.create(
            user=instance,
        )
