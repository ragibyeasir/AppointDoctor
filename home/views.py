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
    doctor=Doctor.objects.filter(user=username).exists()
    context={
        'uname':username,
        'doctor': doctor
    }
    return render(request,'responsivenavbar.html',context)
def doctor_registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pnumber=request.POST.get('pnumber')
        dob=request.POST.get('dob')
        einfo=request.POST.get('einfo')
        exp=request.POST['expe']
        prinfo=request.POST['occuption']
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        photo=request.POST['photo']
        gender=request.POST.get('gender')
        print(uname,email,pnumber,dob,einfo,exp,prinfo,pass1,pass2,photo,gender)
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            messages.error(request,'username or email is already Exist')
            return redirect('dregistration') 
        elif pass1!=pass2:
            messages.error(request,'Password and Confirm Password is not correct')
            return redirect('dregistration')  
        else:
            pdUser=User(username=uname,email=email,password=pass1)
            pdUser.save()
            doctor=Doctor(date_of_birth=dob,institution=einfo,image=photo,experience=exp,phone_number=pnumber,
                          current_working=prinfo,gender=gender,user=pdUser)
            doctor.save()
            messages.success(request,'Dr '+uname+' Enjoy Our Service')
            return redirect('dlogin')
    return render(request,'Registration.html')
def doctors(request):
    return render(request,'exp.html')
def patient_registration(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pnumber=request.POST.get('pnumber')
        dob=request.POST.get('dob')
        occuption=request.POST.get('occuption')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        gender=request.POST.get('gender')
        print(uname,email,pnumber,dob,pass1,pass2,gender)
        print(request.POST)
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            messages.error(request,'username or email is already Exist')
            return redirect('pregistration')
        elif pass1!=pass2:
            messages.error(request,'Password and Confirm Password is not correct')
            return redirect('pregistration')        
        else:
            pdUser=User(username=uname,email=email,password=pass1)
            pdUser.save()
            patient=Patient(occutpion=occuption,phone_numer=pnumber,date_of_birth=dob,gender=gender,user=pdUser)
            patient.save()
            messages.success(request,uname+' Enjoy Our Service')               
            return redirect('plogin')
    return render(request,'userregistration.html')
def login_view(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']
        print(uname,password)
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
    return redirect('login')
