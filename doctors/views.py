from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from doctors.models import *
from doctors.forms import *
from django.core.mail import send_mail
from django.conf import settings
import uuid
# Create
def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forgot_password_token = token).first()
        print(token)
        # print(profile_obj.user.id,profile_obj.forgot_password_tok)
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')
                            
            
            user_obj = User.objects.get(id= user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change-password.html' , context)

def doctor_registration(request):
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
def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
            
            user_obj = User.objects.get(username = username)
            print(user_obj.username, user_obj.first_name)
            token = str(uuid.uuid4())
            profile_obj=Profile.objects.filter(user=user_obj)
            if profile_obj.exists():
                profile_obj=Profile.objects.get(user=user_obj)
            else:
                profile_obj=Profile(user=user_obj)
            # profile_obj=Profile.objects.get(user=user_obj)
            profile_obj.forgot_password_token=token
            
            profile_obj.save()
            
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget-password.html')
def view_profile(request,id):
    user=request.user
    doctor=Doctor.objects.get(user=id)

    print(doctor)
    return render(request,'doctor_profile.html',{
        'doctor':doctor,
        'username':user
    })
    
