from distutils.command.upload import upload
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Teacher(models.Model):
    First_Name=models.CharField(max_length=250,null=False,blank=False)
    Last_Name=models.CharField(max_length=250,null=False,blank=False)
    Profile_Picture=models.ImageField(upload_to='uploads', null=True, blank=True)
    Email_Address=models.EmailField(unique=True,null=False,blank=False)
    Phone_Number = PhoneNumberField(unique = True, null = False, blank = False)
    Room_Number=models.CharField(max_length=10,null=False,blank=False)
    Subjects_taught=models.CharField(max_length=250,null=False,blank=False)

