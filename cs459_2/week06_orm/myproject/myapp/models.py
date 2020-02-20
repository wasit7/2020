from django.db import models

# Create your models here.
class Bike(models.Model):
    start=models.DateField(auto_now=False, auto_now_add=True)
    type=models.CharField(max_length=10)
    price=models.DecimalField( max_digits=8, decimal_places=2)

    def __str__(self):
        return "bike_%s %s"%(self.id, self.type)

class Customer(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    mobile=models.CharField(max_length=20)
    def __str__(self):
        return "customer_%s %s"%(self.id, self.name)

class Rent(models.Model):
    start=models.DateTimeField(auto_now=False, auto_now_add=True)
    stop=models.DateTimeField(auto_now=False, auto_now_add=False)
    cost=models.DecimalField( max_digits=5, decimal_places=2)
    customer=models.ForeignKey( Customer, on_delete=models.CASCADE)
    bike=models.ForeignKey( Bike, on_delete=models.CASCADE)
    def __str__(self):
        return "rent_%s %s"%(self.id, self.cost)

