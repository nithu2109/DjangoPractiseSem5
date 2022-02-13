from django.db import models

# Create your models here.
class OTP(models.Model):
    email = models.EmailField(max_length=100)
    Otp =  models.IntegerField()
    
    def __str__(self):
        return self.email
