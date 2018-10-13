from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('googledaa1a08a6e0e76d3.html', views.gverification, name='verification')
]