from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    url(r'^(?P<slug>[-\w]+)$', views.AlbumDetail.as_view(), name='album'),  # app.views.AlbumView.as_view()
]