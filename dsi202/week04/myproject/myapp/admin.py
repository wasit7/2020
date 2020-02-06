from django.contrib import admin
from .models import Property, Rent, Customer
# Register your models here.
admin.site.register(Property)
admin.site.register(Rent)
admin.site.register(Customer)