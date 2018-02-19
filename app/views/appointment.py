import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages

from app.models import Patient, Doctor, Appointment
from app.forms import SignUpForm, LoginForm, AppointmentForm


class AppointmentView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = AppointmentForm()
        return render(request, 'app/appointment.haml', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_list = list(Appointment.objects.filter( datetime__gte = form.cleaned_data['datetime'] - datetime.timedelta(hours=1) ).filter( datetime__lte = form.cleaned_data['datetime'] + datetime.timedelta(hours=1) ).filter(doctor=form.cleaned_data['doctor']))
#            import ipdb; ipdb.set_trace()
            if appointment_list:
                messages.error(request, "Doctor is busy during this time.")
                return render(request, 'app/appointment.haml', {'form': form})
            else:
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




