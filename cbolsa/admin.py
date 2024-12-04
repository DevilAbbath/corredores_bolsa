from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Accion, Transaccion


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]
 

# Personalización de la visualización de Accion en el admin
class AccionAdmin(admin.ModelAdmin):
    list_display = ('simbolo', 'nombre_empresa', 'precio_actual', 'cambio_porcentual', 'fecha_actualizacion')
    list_filter = ('simbolo',)  # Filtros laterales por símbolo
    search_fields = ('simbolo', 'nombre_empresa')  # Campos de búsqueda
    ordering = ('simbolo',)  # Orden alfabético por símbolo

# Personalización de la visualización de Transaccion en el admin
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'accion', 'tipo_transaccion', 'cantidad', 'precio', 'fecha_transaccion')
    list_filter = ('tipo_transaccion', 'fecha_transaccion')  # Filtros laterales
    search_fields = ('usuario__username', 'accion__simbolo')  # Campos de búsqueda
    ordering = ('-fecha_transaccion',)  # Orden por defecto (más reciente primero)
    
admin.site.unregister(User)  # Desregistra el User admin para agregar el personalizado
admin.site.register(User, CustomUserAdmin)
admin.site.register(Accion, AccionAdmin)
admin.site.register(Transaccion, TransaccionAdmin)