from django.utils.translation import gettext_lazy as _
from django.forms import ModelChoiceField, PasswordInput, SplitDateTimeWidget, ModelForm, DateTimeInput, Textarea, BooleanField

from .models import User, Profile, Appointment

class ProfileForm(ModelForm):
    is_doctor = BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': PasswordInput, 
        }


class LoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': PasswordInput, 
        }


class AppointmentForm(ModelForm):
    doctor = ModelChoiceField(queryset = User.objects.filter(profile__is_doctor=True))
    
    class Meta:
        model = Appointment
        fields = ('datetime',)
        widgets = {
            'datetime': SplitDateTimeWidget, 
        }





