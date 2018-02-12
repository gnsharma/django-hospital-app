from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.forms import DateTimeField, EmailField, ChoiceField, CharField, Form, ModelChoiceField, PasswordInput, SplitDateTimeWidget, ModelForm, DateTimeInput, Textarea, BooleanField
from django.utils import timezone

from .models import Doctor, Patient, Appointment


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
    #    doctors = Doctor.objects.all()
    #    choice_list = []
    #    for doctor in doctors:
    #        choice_list.append((doctor.id, doctor))
    #
    #    doctor_choices = ChoiceField(choices=choice_list)
    #    datetime = DateTimeField( initial=timezone.now())
    doctor = ModelChoiceField(queryset=Doctor.objects.all())

    class Meta:
        model = Appointment
        fields = ['datetime', 'doctor']
#        widgets = {
#            'datetime': SplitDateTimeWidget,
#        }
