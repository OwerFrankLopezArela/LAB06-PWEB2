# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.destinos_turisticos, name='destinos_turisticos'),
    path('destino/<int:destino_id>/', views.detalle_destino, name='detalle_destino'),
]
