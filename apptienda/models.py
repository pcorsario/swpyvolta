from django.db import models


class Customer(models.Model):
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    
class Student(models.Model):
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    

