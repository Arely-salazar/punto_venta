from django.db import models

# Create BD

class Usuario(models.Model):
    id_usuario = models.CharField(max_length=20, unique=True, null=False)
    nombre = models.CharField(max_length=200, null=False)
    apellido =  models.CharField(max_length=200, null=False)
    contrasena =  models.CharField(max_length=200, null=False)
    correo =  models.CharField(max_length=50, unique=True, null=False)
    matricula = models.CharField(max_length=20, unique=True, null=False)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_productos = models.CharField(max_length=20, unique=True, null=False)
    nombre =   models.CharField(max_length=255, null=False)
    precio =  models.DecimalField(max_digits=13, decimal_places=2, null= False)
    cantidad =  models.DecimalField(max_digits=15, decimal_places=2, null= False)
    descripcion = models.CharField(max_length=255, null=False)
    imagen = models.ImageField(upload_to='productos', null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.descripcion

class detalle_Venta(models.Model):
    id_detalle_venta = models.CharField(max_length=50, unique=True, null=False)
    venta = models.ForeignKey('Ventas', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_unitario =  models.DecimalField(max_digits=15, decimal_places=2, null= False)
    cantidad =  models.CharField(max_length=50, null=False)
    descargado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='productos', null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'

    def __str__(self):
        return self.id_detalle_Venta

    
class Rol(models.Model):
    id_rol = models.CharField(max_length=50, unique=True, null=False)
    rol =  models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.rol

class Ventas(models.Model):
    id_Venta = models.CharField(max_length=50, unique=True, null=False)
    clave_transaccion =  models.CharField(max_length=255, null=False)
    paypal_datos =  models.CharField(max_length=255, null=False)
    fecha_venta = models.DateField(null=False)
    correo = models.CharField(max_length=255, null=False)
    total = models.DecimalField(max_digits=15, decimal_places=2, null= False)
    estatus = models.CharField(max_length=255, null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return self.id_Venta

  