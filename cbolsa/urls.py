from django.urls import path
from .views import index, custom_login, custom_logout, dashboard_view, editar_perfil, registro, comprar_accion, venta_accion, ver_portafolio, historial_transacciones

urlpatterns = [
    
    # Neutral Pages
    path('', index, name='index'),
    path('dashboard/',dashboard_view, name='dashboard'),
    
    # URLS para gestion de usuairio
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),   
    path('perfil/', editar_perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    
    # Gestion Acciones
    path('comprar-accion/<int:accion_id>/', comprar_accion, name='comprar_accion'),
    path('vender-accion/<int:accion_id>/', venta_accion, name='venta_accion'),
    path('portafolio/', ver_portafolio, name='portafolio'),
    path('historial-transacciones/', historial_transacciones, name='historial_transacciones'),
]