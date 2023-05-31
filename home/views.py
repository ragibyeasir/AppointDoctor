# from email.message import EmailMessage
# from readline import get_current_history_length
# from tokenize import generate_tokens
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from patient.models import *
from doctors.models import *
from django.contrib import messages
from doctors.forms import *
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
    doctors=Doctor.objects.all()
    context={
        'uname':username,
        'doctors':doctors
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
        doctor1 =Doctor.objects.filter(user=our_user)
        patient1=Patient.objects.filter(user=our_user)
        # print(is_doctor.values(),is_patient.values())

        print(our_user.first_name)        
        context={
            'doctor':doctor1,
            'patient':patient1,
        }
        is_doctor=Doctor.objects.filter(user=our_user).exists()
        is_patient=Patient.objects.filter(user=our_user).exists()
        if is_doctor:
            if request.method=='POST':
                fullname=request.POST['fullname']
                spaciality=request.POST.get('speciality',False)
                pnumber=request.POST.get('pnumber')
                dob=request.POST.get('dob')
                study=request.POST.get('study',False)
                exp=request.POST.get('expe',False)
                occuption=request.POST.get('occuption')
                nid=request.POST.get('nid',False)
                description=request.POST.get('description',False)
                form=ImageForm(request.POST,request.FILES)
                if form.is_valid():
                    img=form.save()
                context['form']=form
                category=Category(category=spaciality)
                category.save()
                doctor=Doctor.objects.filter(user=our_user)
                doctor.update(date_of_birth=dob,study=study,experience=exp,phone_number=pnumber,
                current_working=occuption,nid=nid,category=category,description=description)
                messages.success(request,'Dr'+fullname+'\n Your Information Successfully Updated ')
                return redirect('profile')
        if is_patient:
            if request.method=='POST':
                fullname=request.POST.get('fullname')
                pnumber=request.POST.get('pnumber')
                dob=request.POST.get('dob')
                occuption=request.POST.get('occuption')
                patient=Patient.objects.filter(user=our_user)
                patient.update(occupation=occuption,phone_number=pnumber,date_of_birth=dob)
                messages.success(request,fullname+'\n Your Information Successfully Updated ')
                return redirect('profile')
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
