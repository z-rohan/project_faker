from django.db import models

# Create your models here.

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    email=models.CharField(max_length=40)

    