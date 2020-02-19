from django.urls import path
from .views import *

urlpatterns = [
    path('', list_bike, name='list'),
    path('create/', create_bike, name='create'),
    path('add_bike/', add_bike, name='add_bike'),
    path('edit/<int:id>', edit_bike, name='edit'),
    path('update/', update_bike, name='update'),
]