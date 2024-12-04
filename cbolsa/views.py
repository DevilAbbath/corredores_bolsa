from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.db import models
from .models import UserProfile, Accion, Transaccion
from .forms import CustomUserCreationForm, AccionForm

# Create your views here.
def index(request):
    return render(request, 'cbolsa/index.html')

def custom_logout(request):
    # Cerrar sesión
    logout(request)
    # Redirigir a una página de confirmación
    return render(request, 'registration/logout.html')

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)           
            if login:
                return redirect('dashboard') 
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('index')  # Cambia a la URL que desees
    else:
        form = CustomUserCreationForm()
    return render(request, 'cbolsa/registro.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        email = request.POST.get('email')
        saldo = request.POST.get('saldo')

        # Actualizar datos del usuario
        request.user.email = email
        request.user.save()

        # Actualizar datos del perfil
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.saldo = saldo
        user_profile.save()

        messages.success(request, "Tu perfil ha sido actualizado correctamente.")
        return redirect('index')

    return render(request, 'cbolsa/perfil.html')



# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'cbolsa/dashboard.html')



# Compra de Acciones
@login_required
def comprar_accion(request, accion_id):
    accion = Accion.objects.get(id=accion_id)  # Obtener la acción a comprar
    user_profile = UserProfile.objects.get(user=request.user)  # Perfil del usuario

    if request.method == 'POST':
        cantidad_str = request.POST.get('cantidad')
        if cantidad_str:
            try:
                cantidad = int(cantidad_str)  # Intentar convertir la cantidad a entero
            except ValueError:
                messages.error(request, "La cantidad debe ser un número válido.")
                return redirect('comprar_accion', accion_id=accion_id)
        else:
            messages.error(request, "Por favor ingresa una cantidad de acciones.")
            return redirect('comprar_accion', accion_id=accion_id)

        total_precio = accion.precio_actual * cantidad

        if total_precio > user_profile.saldo:
            messages.error(request, "No tienes suficiente saldo para esta compra.")
            return redirect('comprar_accion', accion_id=accion_id)

        # Realizar la transacción
        user_profile.saldo -= total_precio  # Descontar saldo
        user_profile.save()

        # Crear registro de la transacción
        Transaccion.objects.create(
            usuario=request.user,
            accion=accion,
            tipo_transaccion='COMPRA',
            cantidad=cantidad,
            precio=accion.precio_actual,
        )

        messages.success(request, f"Compra realizada con éxito. Has adquirido {cantidad} acciones de {accion.nombre_empresa}.")
        return redirect('perfil')  # Redirigir al perfil del usuario

    context = {
        'accion': accion,
        'saldo_disponible': user_profile.saldo,
    }
    return render(request, 'cbolsa/comprar_accion.html', context)

# Venta de Acciones
@login_required
def venta_accion(request, accion_id):
    accion = Accion.objects.get(id=accion_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        cantidad_str = request.POST.get('cantidad', "").strip()
        if not cantidad_str.isdigit():
            messages.error(request, "Por favor, ingresa una cantidad válida.")
            return redirect('venta_accion', accion_id=accion_id)

        cantidad = int(cantidad_str)

        transacciones = Transaccion.objects.filter(usuario=request.user, accion=accion, tipo_transaccion='COMPRA')
        cantidad_comprada = sum([t.cantidad for t in transacciones])
        cantidad_vendida = sum(
            [t.cantidad for t in Transaccion.objects.filter(usuario=request.user, accion=accion, tipo_transaccion='VENTA')]
        )
        cantidad_disponible = cantidad_comprada - cantidad_vendida

        if cantidad > cantidad_disponible:
            messages.error(request, "No tienes suficientes acciones para vender.")
            return redirect('venta_accion', accion_id=accion_id)

        precio_venta = accion.precio_actual * (1 + accion.cambio_porcentual / 100)

        user_profile.saldo += precio_venta * cantidad
        user_profile.save()

        Transaccion.objects.create(
            usuario=request.user,
            accion=accion,
            tipo_transaccion='VENTA',
            cantidad=cantidad,
            precio=precio_venta,
        )

        messages.success(
            request,
            f"Venta realizada con éxito. Has vendido {cantidad} acciones de {accion.nombre_empresa} a {precio_venta:.2f} cada una."
        )
        return redirect('perfil')

    transacciones = Transaccion.objects.filter(usuario=request.user, accion=accion, tipo_transaccion='COMPRA')
    cantidad_comprada = sum([t.cantidad for t in transacciones])
    cantidad_vendida = sum(
        [t.cantidad for t in Transaccion.objects.filter(usuario=request.user, accion=accion, tipo_transaccion='VENTA')]
    )
    cantidad_disponible = cantidad_comprada - cantidad_vendida

    context = {
        'accion': accion,
        'saldo_disponible': user_profile.saldo,
        'cantidad_disponible': cantidad_disponible,
    }
    return render(request, 'cbolsa/venta_accion.html', context)

# vista Portafolio
@login_required
def ver_portafolio(request):
    # Obtener el perfil del usuario logueado
    user_profile = UserProfile.objects.get(user=request.user)
    
    # Obtener todas las acciones que el usuario posee
    transacciones = Transaccion.objects.filter(usuario=request.user)
    acciones = Accion.objects.all()
    
    # Calcular el portafolio del usuario (acciones que posee y su cantidad)
    portafolio = []
    for accion in acciones:
        # Calcular cantidad de compras y ventas
        compras = transacciones.filter(accion=accion, tipo_transaccion='COMPRA').aggregate(cantidad=models.Sum('cantidad'))['cantidad'] or 0
        ventas = transacciones.filter(accion=accion, tipo_transaccion='VENTA').aggregate(cantidad=models.Sum('cantidad'))['cantidad'] or 0
        cantidad = compras - ventas
        valor_total = accion.precio_actual * cantidad  # Calcular el valor total de las acciones
        
        portafolio.append({
            'accion': accion,
            'cantidad': cantidad,
            'valor_total': valor_total,
            'compras': compras,
            'ventas': ventas,
        })
    
    return render(request, 'cbolsa/portafolio.html', {'portafolio': portafolio})

# Historial Transacciones
@login_required
def historial_transacciones(request):
    transacciones = Transaccion.objects.filter(usuario=request.user).order_by('-fecha_transaccion')

    context = {
        'transacciones': transacciones,
    }

    return render(request, 'cbolsa/historial_transacciones.html', context)

# Crear Acciones
@login_required
def crear_accion(request):
    # Validar si el usuario es administrador
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if user_profile.tipo_usuario != 'admin':
        return HttpResponseForbidden("No tienes permisos para crear acciones.")

    if request.method == 'POST':
        form = AccionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Acción creada exitosamente.")
            return redirect('dashboard')
    else:
        form = AccionForm()

    return render(request, 'cbolsa/crear_accion.html', {'form': form})