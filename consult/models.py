from django.db import models
from django.contrib.auth.models import User
from doctors.models import *
from patient.models import *
# Create your models here.
class Consult(models.Model):
    doctor=models.ForeignKey(Doctor,models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,models.CASCADE,null=True)
    time=models.DateTimeField()
    def __str__(self):
        return 'Consulting Dr '+str(self.doctor)+' and '+str(self.patient)
class Chat(models.Model):
    doctor=models.ForeignKey(Doctor,models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,models.CASCADE,null=True)  
    chat=models.TextField()
    def __str__(self):
        return 'Chatting Dr '+str(self.doctor)+' with '+str(self.patient)  
class Prescription(models.Model):
    doctor=models.ForeignKey(Doctor,models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,models.CASCADE,null=True)
    prescription=models.TextField()
    def __str__(self):
        return 'Prescription Writting Dr '+str(self.doctor)+' to '+str(self.patient)  
