from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta,date


# Create your models here.
class library(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    SName=models.CharField(max_length=30)    
    StPhone=models.IntegerField()
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.SName
    

class student(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    SDName=models.CharField(max_length=30)   
    SDPhone=models.IntegerField()
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.SDName
    

class notes(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    BookNo=models.IntegerField()
    Image=models.ImageField(upload_to="images")    
    BookName=models.CharField(max_length=50)
    Category=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Return=models.IntegerField()
    Fine=models.IntegerField()
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.BookName

class staff_select(models.Model):
    User = models.CharField(max_length=30)
    book = models.CharField(max_length=30)
    BookNo=models.IntegerField()
    Image=models.ImageField(upload_to="images")    
    BookName=models.CharField(max_length=50)
    Category=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Return=models.IntegerField()
    Date = models.DateField(max_length=50)
    Fine=models.IntegerField()
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.BookName

    


class stud_select(models.Model):
    User = models.CharField(max_length=30)
    book = models.CharField(max_length=30)
    BookNo=models.IntegerField()
    Image=models.ImageField(upload_to="images")    
    BookName=models.CharField(max_length=50)
    Category=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)
    Return=models.IntegerField()
    Date1 = models.CharField(max_length=30)
    Fine=models.IntegerField()
    status = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.BookName
    


class staff_Ret(models.Model):
    user = models.CharField(max_length=30)
    book = models.CharField(max_length=30)
    BookName = models.CharField(max_length=50)
    BookNo = models.CharField(max_length=30)
    Date = models.DateField()
    RetDate = models.DateField()
    Fine = models.IntegerField()
   
    def __str__(self):
        return self.BookName    




    

    
    