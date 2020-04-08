from django.shortcuts import render

def index(request):
    name='Wasit'
    context = {'name': name}
    return render(request, 'index.html', context)