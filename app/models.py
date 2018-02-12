from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='doctor', on_delete=models.CASCADE)
