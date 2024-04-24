from django.shortcuts import render

# Create your views here.

def inicio_view(request):
    return render(request, 'inicio.html')

def ventas_view(request):
    return render(request, 'ventas.html')

def clientes_view(request):
    return render(request, 'clientes.html')

