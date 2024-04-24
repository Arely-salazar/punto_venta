from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='Inicio'),
    path('ventas/', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
]