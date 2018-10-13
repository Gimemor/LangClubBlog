from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:post_id>', views.read, name='read')
]

