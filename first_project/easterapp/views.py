from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "easter.html", {"easter": now.month==3 and now.date==31})