from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol == 'Alumno':
                return redirect('Clientes')
            elif user.rol == 'Administrador':
                return redirect('Ventas')
        else:
            # Manejar el caso en que las credenciales sean incorrectas
            return render(request, 'login.html', {'error_message': 'Credenciales incorrectas'})
    else:
        return render(request, 'login.html')

@login_required
def clientes_view(request):
    # Lógica para obtener datos específicos del alumno si es necesario
    return render(request, 'clientes.html')

@login_required
def ventas_view(request):
    # Lógica para obtener datos específicos del administrador si es necesario
    return render(request, 'base.html')
