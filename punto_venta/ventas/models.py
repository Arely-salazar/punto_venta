from django.db import models

# Create BD

class Usuario(models.Model):
    id_Usuario = models.CharField(max_length=20, unique=True, null=False)
    nombre = models.CharField(max_length=200, null=False)
    apellido =  models.CharField(max_length=200, null=False)
    contrasena =  models.CharField(max_length=200, null=False)
    correo =  models.CharField(max_length=50, unique=True, null=False)
    matricula = models.CharField(max_length=20, unique=True, null=False)
    id_Facultad =  models.CharField(max_length=20, unique=True, null=False)
    id_Rol = models.CharField(max_length=20, unique=True, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_Productos = models.CharField(max_length=20, unique=True, null=False)
    nombre =   models.CharField(max_length=255, null=False)
    precio =  models.DecimalField(max_digits=13, decimal_places=2, null= False)
    cantidad =  models.DecimalField(max_digits=15, decimal_places=2, null= False)
    descripcion = models.CharField(max_length=255, null=False)
    imagen = models.ImageField(upload_to='productos', null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.descripcion

class detalle_Venta(models.Model):
    id_Detalle_De_Venta = models.CharField(max_length=50, unique=True, null=False)
    id_ventas =  models.CharField(max_length=50, null=False)
    id_productos =  models.CharField(max_length=50, null=False)
    precio_Unitario =  models.DecimalField(max_digits=15, decimal_places=2, null= False)
    cantidad =  models.CharField(max_length=50, null=False)
    descargado = models.CharField(max_length=50, null=False)
    imagen = models.ImageField(upload_to='productos', null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'detalle_Venta'
        verbose_name_plural = 'detalles_Ventas'

    def __str__(self):
        return self.id_Detalle_De_Venta


class Facultad(models.Model):
    id_Facultad = models.CharField(max_length=50, unique=True, null=False)
    nombre =  models.CharField(max_length=255, null=False)
    ubicacion =  models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'

    def __str__(self):
        return self.nombre
    
class Roles(models.Model):
    id_Rol = models.CharField(max_length=50, unique=True, null=False)
    rol =  models.CharField(max_length=255, null=False)
    ubicacion =  models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.rol

class Ventas(models.Model):
    id_Ventas = models.CharField(max_length=50, unique=True, null=False)
    clave_Transaccion =  models.CharField(max_length=255, null=False)
    paypal_Datos =  models.CharField(max_length=255, null=False)
    fecha = models.DateField(max_length=255, null=False)
    Correo = models.CharField(max_length=255, null=False)
    Total = models.DecimalField(max_digits=15, decimal_places=2, null= False)
    estatus = models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return self.id_Ventas

  