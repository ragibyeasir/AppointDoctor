from django.db import models
from django.db.models.signals import *
from django.contrib.auth.models import User
# Create your models here.
GENDER=[
    ('M','Male'),
    ('F','Female')
    ]
EINFO=[
    ('MBBS','MBBS'),
    ('BDS','BDS'),
    ('MD','MD'),
    ('FCPS','FCPS')
]
class Category(models.Model):
    category=models.CharField(max_length=150)
    def __str__(self):
        return self.category
class Image(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to='doctorprofile/')
class Doctor(models.Model):#create table
    date_of_birth=models.DateField()
    experience=models.IntegerField()
    phone_number=models.CharField(max_length=11)
    current_working=models.CharField(max_length=50)
    total_consult=models.IntegerField(default=0)
    nid=models.CharField(max_length=17)
    study=models.CharField(max_length=50,choices=EINFO)
    description=models.TextField(max_length=150,null=True)
    gender=models.CharField(max_length=10,choices=GENDER,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    dimage=models.ForeignKey(Image,on_delete=models.CASCADE, null=True,blank=True,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def consult_increase(self):
        self.total_consult=self.total_consult+1
    def __str__(self):
        return str(self.user)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    forgot_password_token=models.CharField(max_length=110)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.forgot_password_token


