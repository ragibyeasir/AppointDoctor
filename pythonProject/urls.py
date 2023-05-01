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
import home.views as hv 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/',hv.user_registration_view,name='uregistration'),
    path('doctor_re/',hv.doctor_registration,name='dregistration'),
    path('patient_re/',hv.patient_registration,name='pregistration'),
    path('', hv.home_page_view,name='home'),
    path('login/',hv.login_view,name='login'),
    path('Doctors/',hv.doctors,name='doctors'),
    path('LogOut/',hv.logout_view,name='logout')
    
]
