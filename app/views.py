from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import Profile, Appointment
from .forms import ProfileForm, LoginForm, AppointmentForm 


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.haml')


class SignUpView(View):
    
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'app/signup.haml', {'form': form}) 

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user._is_doctor = form.cleaned_data['is_doctor']
            user.save()
            return HttpResponseRedirect(reverse('app:home'))
        else:
            print("form is not valid")
            return render(request, 'app/signup.haml', {'form': form})


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'app/login.haml', {'form': form})

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.profile.is_doctor is True:
                    return HttpResponseRedirect(reverse('app:doctor', args=(user.id,)))
                else:
                    return HttpResponseRedirect(reverse('app:patient', args=(user.id,)))
            else:
                return HttpResponse("Your account is disabled.")
    
        else:
            print("invalid login details")
            form = LoginForm()
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
            appointment = form.save(commit=False)
            appointment.patient = request.user
            return HttpResponseRedirect(reverse('app:home'))
        else:
            print("form is not valid")
            return render(request, 'app/appointment.haml', {'form': form})








 
