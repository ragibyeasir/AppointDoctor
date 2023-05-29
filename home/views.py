from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from patient.models import *
from doctors.models import *
from django.contrib import messages
def user_registration_view(request):
    return render(request,'UserLogIn.html')
def home_page_view(request):
    username=request.user
    doctor=None
    if request.user.is_authenticated:
        doctor=Doctor.objects.filter(user=username).exists()
    context={
        'uname':username,
        'doctor': doctor
    }
    return render(request,'responsivenavbar.html',context)
def about_view(request):
    return render(request,'about.html')
def doctors(request):
    username=request.user
    context={
        'uname':username
    }
    return render(request,'exp.html',context)
def login_view(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            doctor=Doctor.objects.filter(user=user).exists()
            if doctor:
                messages.success(request,'Welcome Dr '+uname)
                return redirect('home')
            else:
                messages.success(request,'Welcome '+uname)
                return redirect('home')
        else:
            messages.error(request,'username or password incorrect')
            return redirect('login')
    return render(request,'animatedlogin.html')
def logout_view(request):
    logout(request)
    messages.success(request,'Successfully LogOut')
    return redirect('login')
@login_required
def consult(request):       
    username=request.user
    doctor=None
    if request.user.is_authenticated:
        doctor=Doctor.objects.filter(user=username).exists()
    context={
        'uname':username,
        'doctor': doctor
    }
    return render(request,'consult.html',context)
@login_required
def profile_view(request):
    our_user=request.user
    is_doctor=None
    is_patient=None
    if request.user.is_authenticated:
        is_doctor =Doctor.objects.filter(user=our_user)
        is_patient=Patient.objects.filter(user=our_user)
        print(is_doctor.values(),is_patient.values())
        context={
            'doctor':is_doctor,
            'patient':is_patient
        }
    return render(request,'profile.html',context)
@login_required
def password_change_view(request):
    
    if request.method=='POST':
        username = request.user.username
        current_password = request.POST['cpass']
        print(type(username))
        user = authenticate(username=username,password = current_password)

        if user is not None:
            
            current_user = User.objects.get(username=username)
            
            password1 = request.POST['pass1']
            password2 = request.POST['pass2']
            
            
            if password1 == password2:
                current_user.set_password(password1)
                current_user.save()
                messages.success(request,'Password Changed Successfully')  
            else:
                messages.error(request,"New Password and Confirm Password do not match.")
        else:
            messages.error(request,"Current Password does not match.")
        
    
    return render(request, 'password_change.html')
def doctor_profile(request):
    return render(request,'docprofile.html')