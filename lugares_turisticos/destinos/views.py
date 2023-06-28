from PIL import Image
from django.shortcuts import render, redirect
from .models import DestinosTuristicos
from django.shortcuts import render, get_object_or_404

# Create your views here.

def destinos_turisticos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos_turisticos.html', {'destinos': destinos})

def detalle_destino(request, destino_id):
    destino = get_object_or_404(DestinosTuristicos, pk=destino_id)
    return render(request, 'detalle_destino.html', {'destino': destino})