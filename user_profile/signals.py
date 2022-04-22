from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_profile.models import UserProfile


@receiver(post_save, sender=UserProfile)
def resize_image(sender, instance, created, **kwargs):
    if not created:
        try:
            img = Image.open(instance.avatar.path)
            print(instance.avatar.path)
            if img.height > 300 and img.width > 300:
                output_size = (200, 200)
                img.thumbnail(output_size)
                img.save(instance.avatar.path)
        except:
            pass
