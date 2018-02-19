from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from app.models import Patient, Doctor, Appointment
from app.forms import SignUpForm, LoginForm, AppointmentForm


class DoctorSignUpView(View):

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'app/doctor_signup.haml', {'form': form})

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
            doctor = Doctor(user=user)
            doctor.save()
            return HttpResponseRedirect(reverse('app:login'))
        else:
            return render(request, 'app/doctor_signup.haml', {'form': form})


class DoctorView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        appointment_list = list(Appointment.objects.filter(doctor__user=kwargs['id']))
        return render(request, 'app/doctor.haml',
                      {'appointment_list': appointment_list})
