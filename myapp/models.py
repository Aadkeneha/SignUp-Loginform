from django.db import models


class Patient(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    Username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True, blank=True, default="xyz")
    confirmPassword = models.CharField(max_length=50, null=True, blank=True, default="xyz")
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField()
    profileImg = models.FileField(null=True)
    emailId = models.EmailField(default="xyz@gmail.com")


class Doctor(models.Model):
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50, null=True)
    Username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True,blank=True, default="xyz")
    confirmPassword = models.CharField(max_length=50, null=True,blank=True, default="xyz")
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    pincode = models.IntegerField()
    profileImg = models.FileField(null=True)
    emailId = models.EmailField(default="xyz@gmail.com")
