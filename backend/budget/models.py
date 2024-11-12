from django.db import models
from django.db import models
from django.core.validators import EmailValidator
from django import forms

# Create your models here.

class Users(models.Model):
    FirstName = models.CharField(max_length=15, blank = False)
    LastName = models.CharField(max_length=15, blank=False)
    Username = models.CharField(max_length=10, blank=False)
    Password = models.CharField(max_length=15, blank=False)
    Email = models.EmailField(max_length=254, unique=True, blank=False, validators=[EmailValidator()], default="") 
    Birthday = models.CharField(max_length=20) # Changed to DateField
    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Return full name

