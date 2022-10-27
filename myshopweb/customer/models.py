from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=30,null=True,default='')
    phone_number = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True, blank= True)
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    class Meta:
        ordering = ('id', 'email')
    