from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Patient(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)


class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)

#@receiver(post_save, sender=User)
#def create_or_update_doctors(sender, instance, created, **kwargs):
#    is_doctor = hasattr(instance, 'is_doctor')
#    if created:
#        if is_doctor:
#            Doctor.objects.create(user=instance)
#    if is_doctor:
#        instance.doctor.save()
#
#@receiver(post_save, sender=User)
#def create_or_update_patients(sender, instance, created, **kwargs):
#    is_patient = hasattr(instance, 'is_patient')
#    if created:
#        if is_patient:
#            Patient.objects.create(user=instance)
#    if is_patient:
#        instance.patient.save()
#

class Appointment(models.Model):
    datetime = models.DateTimeField(default=timezone.now) 
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='doctor', on_delete=models.CASCADE)
