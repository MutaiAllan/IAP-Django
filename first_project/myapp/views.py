from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def greet(request, name):
    return HttpResponse(f"Hello {name}!")

def temp(request):
    return render(request, "index.html")