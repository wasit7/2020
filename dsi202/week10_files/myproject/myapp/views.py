from django.shortcuts import render

from django.http import HttpResponse
import datetime

def current_datetime(request):
    context = {'now': datetime.datetime.now()}
    return render(request, 'gwd.html', context)