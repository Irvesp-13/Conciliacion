from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *
from .models import Empleado
from django.http import JsonResponse
from django.utils import timezone
from .models import CargaDescarga
from django.contrib.auth.decorators import login_required

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
    
    # Obtener registros de la tabla dosmilsiete
    expedientes = DosMilSiete.objects.all()
    
    return render(request, 'bienvenida.html', {
        'empleado': empleado,
        'expedientes': expedientes,
    })


def cerrar_sesion(request):
    # Eliminar el ID del empleado de la sesión
    if 'empleado_id' in request.session:
        del request.session['empleado_id']
    return redirect('iniciar_sesion')

def agregar_expediente(request):
    # Verificar si el usuario es administrador
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')
    
    if request.method == 'POST':
        # Get the last id_expediente and increment it
        last_expediente = DosMilSiete.objects.order_by('-id_expediente').first()
        new_id = 1 if not last_expediente else last_expediente.id_expediente + 1
        
        nuevo_expediente = DosMilSiete(
            id_expediente=new_id,  # Add this line
            expediente=request.POST['expediente'],
            junta=request.POST['junta'],
            actor=request.POST['actor'],
            demandado=request.POST['demandado'],
            no_se_ha_notificao_a_las_partes=request.POST['no_se_ha_notificao_a_las_partes'],
            empl_no_realizado=request.POST['empl_no_realizado'],
            empl_exhorto=request.POST['empl_exhorto'],
            cde=request.POST['cde'],
            oap=request.POST['oap'],
            desahogo_pruebas=request.POST['desahogo_pruebas'],
            cierre=request.POST['cierre'],
            laudo_dictado=request.POST['laudo_dictado'],
            auto_ejecucion=request.POST['auto_ejecucion'],
            prescripcion=request.POST['prescripcion'],
            regularizar=request.POST['regularizar']
        )
        nuevo_expediente.save()
        messages.success(request, 'Expediente agregado correctamente.')
        return redirect('bienvenida')
    
    return render(request, 'agregar_expediente.html')


def editar_expediente(request, id_expediente):
    if not request.session.get('empleado_id'):
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=request.session['empleado_id'])
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')

    try:
        expediente = get_object_or_404(DosMilSiete, id_expediente=id_expediente)
        
        if request.method == 'POST':
            # Update fields matching DosMilSiete model
            expediente.expediente = request.POST.get('expediente')
            expediente.junta = request.POST.get('junta')
            expediente.actor = request.POST.get('actor')
            expediente.demandado = request.POST.get('demandado')
            expediente.no_se_ha_notificao_a_las_partes = request.POST.get('no_se_ha_notificao_a_las_partes')
            expediente.empl_no_realizado = request.POST.get('empl_no_realizado')
            expediente.empl_exhorto = request.POST.get('empl_exhorto')
            expediente.cde = request.POST.get('cde')
            expediente.oap = request.POST.get('oap')
            expediente.desahogo_pruebas = request.POST.get('desahogo_pruebas')
            expediente.cierre = request.POST.get('cierre')
            expediente.laudo_dictado = request.POST.get('laudo_dictado')
            expediente.auto_ejecucion = request.POST.get('auto_ejecucion')
            expediente.prescripcion = request.POST.get('prescripcion')
            expediente.regularizar = request.POST.get('regularizar')
            
            expediente.save()
            messages.success(request, 'Expediente actualizado correctamente.')
            return redirect('bienvenida')
        
        return render(request, 'editar_expediente.html', {'expediente': expediente})
        
    except DosMilSiete.DoesNotExist:
        messages.error(request, 'El expediente no existe.')
        return redirect('bienvenida')


def crear_empleado(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('bienvenida')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        clave_empleado = request.POST.get('clave_empleado')
        puesto = request.POST.get('puesto')
        if nombre and clave_empleado and puesto:
            if Empleado.objects.filter(clave_empleado=clave_empleado).exists():
                messages.error(request, 'La clave de empleado ya existe.')
            else:
                Empleado.objects.create(
                    nombre=nombre,
                    clave_empleado=clave_empleado,
                    puesto=puesto
                )
                messages.success(request, 'Empleado creado exitosamente.')
                return redirect('crear_empleado')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

    empleados = Empleado.objects.all()
    return render(request, 'crear_empleado.html', {'empleados': empleados})


def editar_expediente(request, id_expediente):
    if not request.session.get('empleado_id'):
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=request.session['empleado_id'])
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')

    try:
        expediente = get_object_or_404(DosMilSiete, id_expediente=id_expediente)
        
        if request.method == 'POST':
            # Update fields matching DosMilSiete model
            expediente.expediente = request.POST.get('expediente')
            expediente.junta = request.POST.get('junta')
            expediente.actor = request.POST.get('actor')
            expediente.demandado = request.POST.get('demandado')
            expediente.no_se_ha_notificao_a_las_partes = request.POST.get('no_se_ha_notificao_a_las_partes')
            expediente.empl_no_realizado = request.POST.get('empl_no_realizado')
            expediente.empl_exhorto = request.POST.get('empl_exhorto')
            expediente.cde = request.POST.get('cde')
            expediente.oap = request.POST.get('oap')
            expediente.desahogo_pruebas = request.POST.get('desahogo_pruebas')
            expediente.cierre = request.POST.get('cierre')
            expediente.laudo_dictado = request.POST.get('laudo_dictado')
            expediente.auto_ejecucion = request.POST.get('auto_ejecucion')
            expediente.prescripcion = request.POST.get('prescripcion')
            expediente.regularizar = request.POST.get('regularizar')
            
            expediente.save()
            messages.success(request, 'Expediente actualizado correctamente.')
            return redirect('bienvenida')
        
        return render(request, 'editar_expediente.html', {'expediente': expediente})
        
    except DosMilSiete.DoesNotExist:
        messages.error(request, 'El expediente no existe.')
        return redirect('bienvenida')


def crear_empleado(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('bienvenida')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        clave_empleado = request.POST.get('clave_empleado')
        puesto = request.POST.get('puesto')
        if nombre and clave_empleado and puesto:
            if Empleado.objects.filter(clave_empleado=clave_empleado).exists():
                messages.error(request, 'La clave de empleado ya existe.')
            else:
                Empleado.objects.create(
                    nombre=nombre,
                    clave_empleado=clave_empleado,
                    puesto=puesto
                )
                messages.success(request, 'Empleado creado exitosamente.')
                return redirect('crear_empleado')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

    empleados = Empleado.objects.all()
    return render(request, 'crear_empleado.html', {'empleados': empleados})


def eliminar_expediente(request, id_expediente):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para eliminar expedientes.')
        return redirect('bienvenida')
    
    try:
        expediente = DosMilSiete.objects.get(id_expediente=id_expediente)
        expediente.delete()
        messages.success(request, 'Expediente eliminado correctamente.')
    except DosMilSiete.DoesNotExist:
        messages.error(request, 'El expediente no existe.')
    
    return redirect('bienvenida')


def editar_empleado(request, id):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    admin = Empleado.objects.get(id=empleado_id)
    if not admin.es_administrador():
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('bienvenida')

    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.clave_empleado = request.POST.get('clave_empleado')
        empleado.puesto = request.POST.get('puesto')
        empleado.save()
        messages.success(request, 'Empleado actualizado correctamente.')
        return redirect('crear_empleado')
    return render(request, 'editar_empleado.html', {'empleado': empleado})

def eliminar_empleado(request, id):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    admin = Empleado.objects.get(id=empleado_id)
    if not admin.es_administrador():
        messages.error(request, 'No tienes permiso para acceder a esta página.')
        return redirect('bienvenida')

    # Prevent self-deletion
    if int(id) == int(empleado_id):
        messages.error(request, 'No puedes eliminar tu propio usuario mientras estás conectado.')
        return redirect('crear_empleado')

    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    messages.success(request, 'Empleado eliminado correctamente.')
    return redirect('crear_empleado')


def cargar_expediente(request):
    if request.method == 'POST':
        empleado_id = request.session.get('empleado_id')
        expediente_id = request.POST.get('expediente_id')
        nombre_carga = request.POST.get('nombre_carga')

        try:
            empleado = Empleado.objects.get(id=empleado_id)
            expediente = DosMilSiete.objects.get(id_expediente=expediente_id)
            
            carga = CargaDescarga(
                empleado=empleado,
                expediente=expediente,
                nombre_carga=nombre_carga
            )
            carga.save()
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

def ver_cargas(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permiso para ver esta página.')
        return redirect('bienvenida')
    
    cargas = CargaDescarga.objects.all().order_by('-fecha')
    return render(request, 'ver_cargas.html', {'cargas': cargas})


# Remove @login_required decorator and keep the function as is
def archivar_expediente(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return JsonResponse({'success': False, 'error': 'Sesión no iniciada'})
    
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador:
        return JsonResponse({'success': False, 'error': 'No tienes permisos para realizar esta acción'})

    if request.method == 'POST':
        try:
            expediente_id = request.POST.get('expediente_id')
            motivo = request.POST.get('motivo')
            
            expediente = DosMilSiete.objects.get(id_expediente=expediente_id)
            
            # Create archive record with all fields as strings
            Archivados.objects.create(
                expediente=expediente.expediente,  # Changed field name to match model
                junta=expediente.junta,
                actor=expediente.actor,
                demandado=expediente.demandado,
                motivo=motivo,
                fecha_archivo=timezone.now()
            )
            
            # Delete from original table
            expediente.delete()
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})

# Remove @login_required decorator and keep the function as is
def ver_archivados(request):
    empleado_id = request.session.get('empleado_id')
    if not empleado_id:
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=empleado_id)
    if not empleado.es_administrador():
        messages.error(request, 'No tienes permisos para ver expedientes archivados')
        return redirect('bienvenida')
    
    archivados = Archivados.objects.all().order_by('-fecha_archivo')
    return render(request, 'ver_archivados.html', {'archivados': archivados, 'empleado': empleado})

