import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Doctor, Patient, Appointment


class SignUpViewTests(TestCase):

    def test_got_signup_template(self):
        response = self.client.get(reverse('app:signup'))
