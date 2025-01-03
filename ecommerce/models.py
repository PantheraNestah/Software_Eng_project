from django.db import models

# Create your models here.
class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    value = models.FloatField()
    pickup_location = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=100, default='Pending')
    pickup_status = models.CharField(max_length=100, default='Pending')
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name

