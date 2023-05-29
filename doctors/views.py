from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from doctors.models import *
from doctors.forms import *
# Create
def doctor_registration(request):
    submitted=False
    if request.method=='POST':
        full_name=request.POST['fullname']
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pnumber=request.POST.get('pnumber')
        dob=request.POST.get('dob')
        einfo=request.POST.get('einfo')
        exp=request.POST['expe']
        prinfo=request.POST['occuption']
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            img=form.save()
        else:
            if 'submitted' in request.GET:
                submitted=True
        gender=request.POST.get('gender')
        if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
            messages.error(request,'username or email is already Exist')
            return redirect('dregistration') 
        elif pass1!=pass2:
            messages.error(request,'Password and Confirm Password is not correct')
            return redirect('dregistration')  
        else:
            pdUser=User(username=uname,email=email,first_name=full_name)
            pdUser.set_password(pass1)
            pdUser.save()
            doctor=Doctor(date_of_birth=dob,study=einfo,dimage=img,experience=exp,phone_number=pnumber,
                          current_working=prinfo,gender=gender,user=pdUser)
            doctor.save()
            messages.success(request,'Dr '+uname+' Enjoy Our Service')
            return redirect('login')
    else:
        form=ImageForm()
    return render(request,'Registration.html',{'forms': form}) 
