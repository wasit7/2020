from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Property
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    html='''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>

        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>

        </body>
        </html>
    '''
    return HttpResponse(html)

def list(request):
    list=""
    for i in Property.objects.all():
        list+="<p>{name} {ac} {size} {price}</p>".format(name=i.name,ac=i.ac,size=i.size,price=i.price_per_day)
    html='''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>

        <h1>List of Properties</h1>
        {list}

        </body>
        </html>
    '''.format(list=list)
    return HttpResponse(html)