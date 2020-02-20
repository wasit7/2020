from django.contrib import admin
from .models import Bike, Customer, Rent
# Register your models here.
admin.site.register(Bike)
admin.site.register(Customer)
admin.site.register(Rent)