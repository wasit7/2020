from django.shortcuts import render, redirect
from .models import Bike, Customer, Rent
# Create your views here.

def list_bike(request):
    data = Bike.objects.all()
    return render(request, 'list_bike.html', {'bike':data})

def create_bike(request):
    return render(request, 'create_bike.html')

def add_bike(request):
    type = request.POST['type']
    price = request.POST['price']
    Bike.objects.create(type=type, price=price)
    return redirect('list')

def edit_bike(request, id):
    data = Bike.objects.get(pk=id)
    return render(request, 'edit_bike.html', {'bike': data})

def update_bike(request):
    id = request.POST['id']
    type = request.POST['type']
    price = request.POST['price']
    Bike.objects.filter(pk=id).update(type=type, price=price)
    return redirect('list')