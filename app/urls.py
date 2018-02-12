from django.urls import path

from .views import HomeView, SignUpView, PatientSignUpView, DoctorSignUpView, LoginView
from .views import LogoutView, DoctorView, PatientView, AppointmentView

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
]
