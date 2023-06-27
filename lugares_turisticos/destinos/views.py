from PIL import Image
from django.shortcuts import render, redirect
from .models import DestinosTuristicos

# Create your views here.

def destinos_turisticos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos_turisticos.html', {'destinos': destinos})
