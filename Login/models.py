from django.db import models

# Create your models here.
class UserData(models.Model):
    email=models.CharField(max_length=255)
    passwd=models.CharField(max_length=20)