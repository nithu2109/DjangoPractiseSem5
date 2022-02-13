from dataclasses import fields
from django import forms
from . import models

class OtpForm(forms.ModelForm):
    class Meta:
        model = models.OTP 
        fields = ['email']
        
    