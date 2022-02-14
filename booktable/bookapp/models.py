from django.db import models

# Create your models here.
class Book(models.Model):
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=20)
    bookprice=models.IntegerField()
    bookpublisher=models.CharField(max_length=50)
