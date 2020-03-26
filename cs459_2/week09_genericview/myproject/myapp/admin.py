from django.contrib import admin
from .models import Bike
# Register your models here.
class BikeAdmin(admin.ModelAdmin):
    list_display = ('start','type','price')

admin.site.register(Bike,BikeAdmin)