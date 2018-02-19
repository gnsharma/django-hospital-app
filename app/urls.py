from django.urls import path

from app.views.common import HomeView, SignUpView, LoginView, LogoutView
from app.views.patient import PatientSignUpView, PatientView
from app.views.doctor import DoctorSignUpView, DoctorView
from app.views.appointment import AppointmentView, DeleteAppointmentView

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signup/patient', PatientSignUpView.as_view(), name='patient-signup'),
    path('signup/doctor', DoctorSignUpView.as_view(), name='doctor-signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('doctor/<int:id>/', DoctorView.as_view(), name='doctor'),
    path('patient/<int:id>/', PatientView.as_view(), name='patient'),
    path('appointment', AppointmentView.as_view(), name='appointment'),
    path('appointment/<int:id>', DeleteAppointmentView.as_view(), name='delete-appointment'),
]
