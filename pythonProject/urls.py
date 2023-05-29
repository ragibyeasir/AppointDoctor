"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import home.views as hv
import doctors.views as dv
import patient.views as pv 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/',hv.user_registration_view,name='uregistration'),
    path('doctor_re/',dv.doctor_registration,name='dregistration'),
    path('patient_re/',pv.patient_registration,name='pregistration'),
    path('', hv.home_page_view,name='home'),
    path('login/',hv.login_view,name='login'),
    path('Doctors/',hv.doctors,name='doctors'),
    path('LogOut/',hv.logout_view,name='logout'),
    path('Consult/',hv.consult,name='consult'),
    path('About/',hv.about_view,name='about'),
    path('Profile/',hv.profile_view,name='profile'),
    path('passwordchange/',hv.password_change_view,name='passchange'),
    path('DoctorProfile/',hv.doctor_profile,name='dprofile')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
