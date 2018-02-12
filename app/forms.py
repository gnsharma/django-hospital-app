from django.forms import ModelChoiceField, EmailField, CharField, Form
from django.forms import PasswordInput, ModelForm

from .models import Doctor, Appointment


class SignUpForm(Form):
    username = CharField(label='User Name', max_length=150,
                         help_text='150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.')
    first_name = CharField(label='First Name', max_length=150)
    last_name = CharField(label='Last Name', max_length=150)
    email = EmailField(label='Email')
    password = CharField(label='Password', widget=PasswordInput, max_length=150)


class LoginForm(Form):
    username = CharField(label='User Name', max_length=150,
                         help_text='150 characters or fewer. Usernames may contain alphanumeric, _, @, +, . and - characters.')
    password = CharField(label='Password', widget=PasswordInput, max_length=150)


class AppointmentForm(ModelForm):
    doctor = ModelChoiceField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['datetime', 'doctor']
