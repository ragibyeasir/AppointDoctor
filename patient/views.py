from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from patient.models import *
# Create your views here.
def patient_registration(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        uname=request.POST.get('username')
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
            pdUser=User(username=uname,email=email,first_name=fullname)
            pdUser.set_password(pass1)
            pdUser.save()
            patient=Patient(occupation=occuption,phone_number=pnumber,date_of_birth=dob,gender=gender,user=pdUser)
            patient.save()
            messages.success(request,uname+' Enjoy Our Service')               
            return redirect('login')
    return render(request,'userregistration.html')