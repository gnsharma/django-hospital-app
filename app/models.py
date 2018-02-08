from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
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
#    user = get_user_model()
#    doctors = user.objects.filter(profile__is_doctor=True)
#    doctor_choices = models.CharField(max_length=254, choices=doctors, null=True)
    datetime = models.DateTimeField(default=timezone.now) 
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor', on_delete=models.CASCADE)
