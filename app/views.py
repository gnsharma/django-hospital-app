from django.shortcuts import get_list_or_404, render
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
            import ipdb; ipdb.set_trace()
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
        import ipdb; ipdb.set_trace()
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
        no_appointments = False
        appointment_list = list(Appointment.objects.filter(patient=kwargs['id'])) 
        if not appointment_list:
            no_appointments = True
        return render(request, 'app/patient.haml', {'no_appointments': no_appointments, 'appointment_list': appointment_list})


class DoctorView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        no_appointments = False
        appointment_list = list(Appointment.objects.filter(doctor = kwargs['id'])) 
        if not appointment_list:
            no_appointments = True
        return render(request, 'app/doctor.haml', {'no_appointments': no_appointments, 'appointment_list': appointment_list})


class AppointmentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = AppointmentForm()
        return render(request, 'app/appointment.haml', {'form': form}) 

    def post(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        form = AppointmentForm(request.POST)
        if form.is_valid():
            import ipdb; ipdb.set_trace()
#            appointment = form.save(commit=False)
#            appointment.patient = request.user
            return HttpResponseRedirect(reverse('app:home'))
        else:
            print("form is not valid")
            return render(request, 'app/appointment.haml', {'form': form})







 
