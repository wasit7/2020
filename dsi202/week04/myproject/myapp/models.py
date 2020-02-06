from django.db import models

class Property(models.Model):
    ac=models.BooleanField()
    size=models.DecimalField(max_digits=5, decimal_places=2)
    price_per_day=models.DecimalField(max_digits=5, decimal_places=2)

class Customer(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=20)
    dob=models.DateField()
    gender=models.BooleanField()

class Rent(models.Model):
    start=models.DateTimeField()
    stop=models.DateTimeField()
    cost=models.DecimalField(max_digits=10,decimal_places=2)
    property=models.ForeignKey(Property, on_delete=models.CASCADE)
    property=models.ForeignKey(Customer, on_delete=models.CASCADE)