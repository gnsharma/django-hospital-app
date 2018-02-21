from django.urls import path

from app.views.common import RedirectView, HomeView, SignUpView, LoginView, LogoutView
from app.views.patient import PatientSignUpView, PatientView
from app.views.doctor import DoctorSignUpView, DoctorView
from app.views.appointment import AppointmentView, DeleteAppointmentView

app_name = 'app'
urlpatterns = [
    path('', RedirectView.as_view(), name='redirect'),
    path('hospital/', HomeView.as_view(), name='home'),
    path('hospital/signup', SignUpView.as_view(), name='signup'),
    path('hospital/signup/patient', PatientSignUpView.as_view(), name='patient-signup'),
    path('hospital/signup/doctor', DoctorSignUpView.as_view(), name='doctor-signup'),
    path('hospital/login', LoginView.as_view(), name='login'),
    path('hospital/logout', LogoutView.as_view(), name='logout'),
    path('hospital/doctor/<int:id>/', DoctorView.as_view(), name='doctor'),
    path('hospital/patient/<int:id>/', PatientView.as_view(), name='patient'),
    path('hospital/appointment/book', AppointmentView.as_view(), name='appointment'),
    path('hospital/appoitnment/<int:id>/delete', DeleteAppointmentView.as_view(), name='delete-appointment'),
]
