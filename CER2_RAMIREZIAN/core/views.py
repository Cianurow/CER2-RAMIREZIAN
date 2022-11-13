from distutils import core
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Correspondencia

# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    correspondencias = Correspondencia.objects.all().order_by('nroResidencia')
    if queryset:
        if Correspondencia.objects.filter(nroResidencia = queryset):
            correspondencias = Correspondencia.objects.filter(nroResidencia = queryset)    
    
    return render(request, 'core/index.html', {'correspondencias':correspondencias})

