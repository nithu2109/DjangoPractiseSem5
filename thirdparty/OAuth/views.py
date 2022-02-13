import email
import smtpd
from django.shortcuts import render
from . import forms,models
import random
import smtplib
# Create your views here.
def index(request):
    form = forms.OtpForm()
    if request.method =="POST":
        form = forms.OtpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            #generate 5 digit number 
            otp=random.randint(10000,99999)
            user = models.OTP(email=email,Otp=otp)
            user.save()
            #send email to user 
        
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login('12xxxx07@sastra.ac.in','password')
            s.sendmail('12xxxx07@sastra.ac.in',email,f'Your OTP is {otp}')
            s.quit()
            return render(request,'otp.html',{'email':email,'otp':otp})
    return render(request,'index.html',{'form':form})
            
            
            
            
        
        