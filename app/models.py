from django.contrib.auth.models import User 
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_doctor = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        is_doctor = getattr(instance, '_is_doctor', None)
        Profile.objects.create(user=instance, is_doctor=is_doctor)
    instance.profile.save()


class Appointment(models.Model):
    datetime = models.DateTimeField(default=timezone.now) 
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor', on_delete=models.CASCADE)
