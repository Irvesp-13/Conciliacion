from django.shortcuts import render, redirect
from django.contrib.auth import login
from .backends import EmpleadoBackend
from .models import *

def iniciar_sesion(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        clave_empleado = request.POST['clave_empleado']
        
        try:
            # Buscar al empleado por su clave de empleado y nombre
            empleado = Empleado.objects.get(clave_empleado=clave_empleado, nombre=nombre)
            
            # Guardar el ID del empleado en la sesión
            request.session['empleado_id'] = empleado.id
            return redirect('bienvenida')
        except Empleado.DoesNotExist:
            # Mostrar mensaje de error si las credenciales son incorrectas
            return render(request, 'iniciar_sesion.html', {'error': 'Credenciales incorrectas'})
    
    return render(request, 'iniciar_sesion.html')

def bienvenida(request):
    # Verificar si el empleado está autenticado
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    # Obtener el empleado autenticado
    empleado = Empleado.objects.get(id=empleado_id)
    
    # Obtener todos los registros de la tabla conciliacion_expadientes
    expedientes = ConciliacionExpedientes.objects.all()
    
    return render(request, 'bienvenida.html', {
        'empleado': empleado,
        'expedientes': expedientes,
    })

def administrador(request):
    # Verificar si el empleado está autenticado
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    # Obtener el empleado autenticado
    empleado = Empleado.objects.get(id=empleado_id)
    
    # Verificar si el empleado es un administrador
    if empleado.puesto != 1:
        return render(request, 'error.html', {'mensaje': 'No tienes permiso para acceder a esta página.'})
    
    return render(request, 'administrador.html')

def cerrar_sesion(request):
    # Eliminar el ID del empleado de la sesión
    if 'empleado_id' in request.session:
        del request.session['empleado_id']
    return redirect('iniciar_sesion')