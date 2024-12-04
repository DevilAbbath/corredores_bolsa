from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Administrador'),
        ('regular', 'Regular'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con User
    tipo_usuario = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='regular')
    saldo = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=100.00)  
    fecha_registro = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.user.username  # Devuelve el nombre de usuario como representación

class Accion(models.Model):
    simbolo = models.CharField(max_length=10, unique=True)
    nombre_empresa = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    cambio_porcentual = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.simbolo 
    
class Transaccion(models.Model):
    TIPOS_TRANSACCION = [
        ('COMPRA', 'Compra'),
        ('VENTA', 'Venta'),
    ]

    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    accion = models.ForeignKey('Accion', on_delete=models.CASCADE)
    tipo_transaccion = models.CharField(max_length=15, choices=TIPOS_TRANSACCION)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.tipo_transaccion} - {self.accion.simbolo}'
