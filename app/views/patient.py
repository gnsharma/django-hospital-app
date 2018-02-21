from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from app.models import Patient, Doctor, Appointment
from app.forms import SignUpForm


class PatientSignUpView(View):

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'app/patient/patient_signup.haml', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user.password = make_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()
            patient = Patient(user=user)
            patient.save()
            return HttpResponseRedirect(reverse('app:login'))
        else:
            return render(request, 'app/patient/patient_signup.haml', {'form': form})


class PatientView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        appointment_list = Appointment.objects.filter(patient__user=kwargs['id'])
        return render(request, 'app/patient/patient.haml',
                      {'appointment_list': appointment_list})
