from django.contrib import admin
from ventas.models import Usuario, Producto, detalle_Venta, Rol, Ventas

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'id_usuario')
    search_fields = ('nombre', 'id_usuario')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_venta', 'venta', 'producto')
    search_fields = ('id_detalle_venta', 'venta__id_venta', 'producto__descripcion')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class RolAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'rol')
    search_fields = ['rol']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id_Venta', 'fecha_venta', 'total')
    search_fields = ['id_Venta']
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(detalle_Venta, DetalleVentaAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Ventas, VentasAdmin)