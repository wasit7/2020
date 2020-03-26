from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    mobile=models.CharField(max_length=20)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('customer_detail', args=[str(self.id)])