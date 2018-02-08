from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('doctor/<int:id>/', views.DoctorView.as_view(), name='doctor'),
    path('patient/<int:id>/', views.PatientView.as_view(), name='patient'),
    path('appointment', views.AppointmentView.as_view(), name='appointment'),
]
