from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
GENDER=[
    ('M','Male'),
    ('F','Female')
    ]
class Category(models.Model):
    category=models.CharField(max_length=30)
    def __str__(self):
        return self.category
class Doctor(models.Model):
    date_of_birth=models.DateField()
    institution=models.CharField(max_length=50)
    image=models.ImageField(upload_to='./doctorprofile/',null=True)
    experience=models.IntegerField()
    phone_number=models.CharField(max_length=11)
    current_working=models.CharField(max_length=50)
    total_consult=models.IntegerField(default=0)
    nid=models.CharField(max_length=17)
    study=models.CharField(max_length=15)
    description=models.TextField(null=True)
    gender=models.CharField(max_length=10,choices=GENDER,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user)

