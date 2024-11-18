from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile

"""
post_save - Göndərən modelin save olunması zamanı çağrılır.
pre_save - Göndərən model save olunmamışdan öncə çağrılır

post_delete - Göndərən modelin obyekti silindikdən sonra çağrılır.
pre_delete - Göndərən modelin obyekti silinməmişdən əvvəl çağrılır.

post_migrate - Göndərən modelin miqrasiyası zamanı çağrılır.
"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
