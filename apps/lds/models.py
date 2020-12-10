
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def post_save_user(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', models.CASCADE, related_name='profile')
    name = models.CharField(_('名稱'), max_length=255, blank=True)
