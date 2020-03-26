from myapp.models import Bike

from django.views.generic.detail import DetailView
class BikeDetailView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'

from django.views.generic import ListView
class BikeListView(ListView):
    model = Bike
    paginate_by = 3
    #queryset=Bike.objects.filter(type='mountain')
    template_name = 'bike_list.html'

from django.views.generic.edit import CreateView
class BikeCreateView(CreateView):
    model = Bike
    template_name = 'bike_create.html'
    fields = ['type','price']

from django.views.generic.edit import UpdateView
class BikeUpdateView(UpdateView):
    model = Bike
    template_name = 'bike_update.html'
    fields = ['type','price']