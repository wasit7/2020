from django.contrib import admin
from .models import Property, Rent, Customer

class RentAdmin(admin.ModelAdmin):
    #list_display=[f.name for f in Rent._meta.fields]
    list_display=['start','stop','cost','property','customer']
admin.site.register(Rent,RentAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Customer._meta.fields]
    list_filter=['gender']
admin.site.register(Customer,CustomerAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display=[f.name for f in Property._meta.fields]
    list_editable=['price_per_day']
admin.site.register(Property,PropertyAdmin)

# admin.site.register(Property)
# admin.site.register(Rent)
# admin.site.register(Customer)