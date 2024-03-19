from django.shortcuts import render
from django.http import HttpResponse
import datetime

tasks = ["Gym", "Lunch", "Code", "Sleep"]

def index(request):
    return render(request, "tasks.html", {"tasks": tasks})

def add(request):
    return render(request, "add.html")