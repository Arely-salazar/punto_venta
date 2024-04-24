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

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto)
admin.site.register(detalle_Venta)
admin.site.register(Rol)
admin.site.register(Ventas)