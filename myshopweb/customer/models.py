from django.db import models
from uuid import uuid4

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    token = models.CharField(max_length=30, blank=True, editable=False, default=uuid4())
    
    def __unicode__(self):
        return self.content
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.content
    def __str__(self):
        return self.name