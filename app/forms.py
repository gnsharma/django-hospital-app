from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, Form, ModelChoiceField, PasswordInput, SplitDateTimeWidget, ModelForm, DateTimeInput, Textarea, BooleanField

from .models import Doctor, Patient, Appointment

class SignUpForm(Form):
    username = CharField(label='User Name', max_length=150, help_text='150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.')
    first_name = CharField(label='First Name', max_length=150)
    last_name = CharField(label='Last Name', max_length=150)
    email = EmailField(label='Email')
    password = CharField(label='Password', widget=PasswordInput, max_length=150)


class LoginForm(Form):
    username = CharField(label='User Name', max_length=150, help_text='150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.')
    password = CharField(label='Password', widget=PasswordInput, max_length=150)
    

class AppointmentForm(ModelForm):
    doctor = ModelChoiceField(queryset = Doctor.objects.all())
    
    class Meta:
        model = Appointment
        fields = ('datetime',)
        widgets = {
            'datetime': SplitDateTimeWidget, 
        }





