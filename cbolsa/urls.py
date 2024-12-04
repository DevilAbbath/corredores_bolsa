from django.urls import path
from .views import index, custom_login, custom_logout, dashboard_view, editar_perfil, registro

urlpatterns = [
    
    # Neutral Pages
    path('', index, name='index'),
    path('dashboard/',dashboard_view, name='dashboard'),
    
    # URLS para gestion de usuairio
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),   
    path('perfil/', editar_perfil, name='perfil'),
    path('registro/', registro, name='registro'),
]