# urls.py

from django.urls import path
from . import views

app_name = 'destinos'

urlpatterns = [
    path('', views.destinos_turisticos, name='destinos_turisticos')
]
