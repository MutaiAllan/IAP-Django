from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name='index'),
    path("about", views.index,name='index'),
    path("time", views.current_datetime, name='current_datetime'),
    path("name/<str:name>", views.greet, name='greet'),
    path("temp", views.temp, name='temp')
]