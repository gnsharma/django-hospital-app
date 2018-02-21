from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from app.models import Patient, Doctor
from app.forms import SignUpForm, LoginForm


class RedirectView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('app:home'))


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
                messages.error(request, "User credentials are not correct.")
                return render(request, 'app/login.haml', {'form': form})
        else:
            return render(request, 'app/login.haml', {'form': form})


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('app:home'))
