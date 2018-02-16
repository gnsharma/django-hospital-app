from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Patient, Doctor, Appointment
from .forms import SignUpForm, LoginForm, AppointmentForm


class HomeView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'doctor'):
                return HttpResponseRedirect(reverse('app:doctor', args=(request.user.id,)))
            if hasattr(request.user, 'patient'):
                return HttpResponseRedirect(reverse('app:patient', args=(request.user.id,)))
        else:
            return render(request, 'app/home.haml')


class SignUpView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/signup.haml', {})


class PatientSignUpView(View):

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'app/patient_signup.haml', {'form': form})

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
            return render(request, 'app/patient_signup.haml', {'form': form})


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


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'app/login.haml', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if hasattr(user, 'doctor'):
                        return HttpResponseRedirect(reverse('app:doctor', args=(user.id,)))
                    elif hasattr(user, 'patient'):
                        return HttpResponseRedirect(reverse('app:patient', args=(user.id,)))
                else:
                    return HttpResponse("Your account is disabled.")

            else:
                form = LoginForm()
                return render(request, 'app/login.haml', {'form': form})
        else:
            return render(request, 'app/login.haml', {'form': form})


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('app:home'))


class PatientView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        appointment_list = list(Appointment.objects.filter(patient__user=kwargs['id']))
        return render(request, 'app/patient.haml',
                      {'appointment_list': appointment_list})


class DoctorView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        appointment_list = list(Appointment.objects.filter(doctor__user=kwargs['id']))
        return render(request, 'app/doctor.haml',
                      {'appointment_list': appointment_list})


class AppointmentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = AppointmentForm()
        return render(request, 'app/appointment.haml', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient = Patient.objects.get(user__id=request.user.id)
            appointment.patient = patient
            appointment.save()
            return HttpResponseRedirect(reverse('app:patient', args=(request.user.id,)))
        else:
            return render(request, 'app/appointment.haml', {'form': form})


class DeleteAppointmentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['id'])
        appointment.delete()
        if hasattr(request.user, 'doctor'):
            return HttpResponseRedirect(reverse('app:doctor', args=(request.user.id,)))
        if hasattr(request.user, 'patient'):
            return HttpResponseRedirect(reverse('app:patient', args=(request.user.id,)))














