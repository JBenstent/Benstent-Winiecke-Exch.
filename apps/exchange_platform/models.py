from django.db import models

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=25)
    aka=models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
