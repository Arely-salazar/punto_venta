from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_view, name='Login'),
    path('ventas/', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
    path('accounts/', include('django.contrib.auth.urls')),
]