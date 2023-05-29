from django.db import models
from django.contrib.auth.models import User
from doctors.models import *
# Create your models here.
class Patient(models.Model):
    occupation=models.CharField(max_length=15)
    phone_number=models.CharField(max_length=11)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER,null=True)
    user=models.ForeignKey(User,models.CASCADE,null=True)
    def __str__(self):
        return str(self.user)
class Feedback(models.Model):
    patient=models.ForeignKey(Patient,models.SET_NULL,null=True)
    doctor=models.ForeignKey(Doctor,models.SET_NULL,null=True)
    feedback=models.TextField(null=True)
    def __str__(self):
        return 'Feedback to '+str(self.doctor)+' by ' +str(self.patient)
