from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from accounts.utils.mails import MailSender
from user_profile.models import UserProfile


@receiver(post_save, sender=User)
def profile_create(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()
