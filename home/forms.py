from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
class UserPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_("Email"), max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email',"class":'form-control'}))
