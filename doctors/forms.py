from django import forms
from django.forms import ModelForm
from .models import *

class ImageForm(ModelForm):
    class Meta:
        model=Image
        fields=('image',)
        labels={
            'image':''
        }