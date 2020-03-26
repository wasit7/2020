from django.shortcuts import render
from django.urls import reverse

from myapp.models import Customer
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_create.html'
    fields = ['name','dob','mobile']
    success_url="/admin"

class CustomerListView(ListView):
    model = Customer
    paginate_by = 3
    #queryset=Customer.objects.filter(type='mountain')
    template_name = 'customer_list.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name','dob','mobile']
    template_name = 'customer_update.html'