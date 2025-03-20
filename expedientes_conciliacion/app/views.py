from django.shortcuts import render, redirect
from django.contrib import messages
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
        # Procesar el formulario para agregar un expediente
        expediente = request.POST['expediente']
        junta = request.POST['junta']
        tomo = request.POST['tomo']
        actor_nombre = request.POST['actor_nombre']
        mujer_numero = request.POST['mujer_numero']
        hombre_numero = request.POST['hombre_numero']
        demandado_nombre = request.POST['demandado_nombre']
        mujer_numero_0 = request.POST['mujer_numero_0']
        hombre_numero_0 = request.POST['hombre_numero_0']
        persona_moral_numero = request.POST['persona_moral_numero']
        iebem = request.POST['iebem']
        servicios_salud = request.POST['servicios_salud']
        poder_ejecutivo = request.POST['poder_ejecutivo']
        ayuntamientos = request.POST['ayuntamientos']
        otros_organismos = request.POST['otros_organismos']
        no_se_ha_notificado_a_las_partes = request.POST['no_se_ha_notificado_a_las_partes']
        empl_no_realizado = request.POST['empl_no_realizado']
        empl_exhorto = request.POST['empl_exhorto']
        exhortos_sin_enviar = request.POST['exhortos_sin_enviar']
        exhortos_cdmx = request.POST['exhortos_cdmx']
        exhortos_foraneos = request.POST['exhortos_foraneos']
        cde = request.POST['cde']
        tercero_llamado_a_juicio = request.POST['tercero_llamado_a_juicio']
        oap = request.POST['oap']
        desahogo_pruebas = request.POST['desahogo_pruebas']
        test_falta_citar = request.POST['test_falta_citar']
        periciales_partes = request.POST['periciales_partes']
        pericial_tercero = request.POST['pericial_tercero']
        inf_falta_hacer = request.POST['inf_falta_hacer']
        inf_falta_desahogar = request.POST['inf_falta_desahogar']
        otras_pruebas = request.POST['otras_pruebas']
        alegatos = request.POST['alegatos']
        prueba_pendiente = request.POST['prueba_pendiente']
        cierre = request.POST['cierre']
        laudo_dictado = request.POST['laudo_dictado']
        absolutorio = request.POST['absolutorio']
        condenatorio = request.POST['condenatorio']
        monto = request.POST['monto']
        auto_ejecucion = request.POST['auto_ejecucion']
        terceria = request.POST['terceria']
        recurso_revision = request.POST['recurso_revision']
        remate = request.POST['remate']
        inactividad_1_anio = request.POST['inactividad_1_anio']
        inactividad_2_anios_mas = request.POST['inactividad_2_anios_mas']
        amparo_indirecto = request.POST['amparo_indirecto']
        amparo_directo_cumpl = request.POST['amparo_directo_cumpl']
        sustitucion_patronal = request.POST['sustitucion_patronal']
        no_interpuesta = request.POST['no_interpuesta']
        prescripcion = request.POST['prescripcion']
        depuracion = request.POST['depuracion']
        regularizar = request.POST['regularizar']
        reviso_capturo = request.POST['reviso_capturo']
        
        nuevo_expediente = ConciliacionExpedientes(
            expediente=expediente,
            junta=junta,
            tomo=tomo,
            actor_nombre=actor_nombre,
            mujer_numero=mujer_numero,
            hombre_numero=hombre_numero,
            demandado_nombre=demandado_nombre,
            mujer_numero_0=mujer_numero_0,
            hombre_numero_0=hombre_numero_0,
            persona_moral_numero=persona_moral_numero,
            iebem=iebem,
            servicios_salud=servicios_salud,
            poder_ejecutivo=poder_ejecutivo,
            ayuntamientos=ayuntamientos,
            otros_organismos=otros_organismos,
            no_se_ha_notificado_a_las_partes=no_se_ha_notificado_a_las_partes,
            empl_no_realizado=empl_no_realizado,
            empl_exhorto=empl_exhorto,
            exhortos_sin_enviar=exhortos_sin_enviar,
            exhortos_cdmx=exhortos_cdmx,
            exhortos_foraneos=exhortos_foraneos,
            cde=cde,
            tercero_llamado_a_juicio=tercero_llamado_a_juicio,
            oap=oap,
            desahogo_pruebas=desahogo_pruebas,
            test_falta_citar=test_falta_citar,
            periciales_partes=periciales_partes,
            pericial_tercero=pericial_tercero,
            inf_falta_hacer=inf_falta_hacer,
            inf_falta_desahogar=inf_falta_desahogar,
            otras_pruebas=otras_pruebas,
            alegatos=alegatos,
            prueba_pendiente=prueba_pendiente,
            cierre=cierre,
            laudo_dictado=laudo_dictado,
            absolutorio=absolutorio,
            condenatorio=condenatorio,
            monto=monto,
            auto_ejecucion=auto_ejecucion,
            terceria=terceria,
            recurso_revision=recurso_revision,
            remate=remate,
            inactividad_1_anio=inactividad_1_anio,
            inactividad_2_anios_mas=inactividad_2_anios_mas,
            amparo_indirecto=amparo_indirecto,
            amparo_directo_cumpl=amparo_directo_cumpl,
            sustitucion_patronal=sustitucion_patronal,
            no_interpuesta=no_interpuesta,
            prescripcion=prescripcion,
            depuracion=depuracion,
            regularizar=regularizar,
            reviso_capturo=reviso_capturo   
        )
        nuevo_expediente.save()
        messages.success(request, 'Expediente agregado correctamente.')
        return redirect('bienvenida')
    
    return render(request, 'agregar_expediente.html')

