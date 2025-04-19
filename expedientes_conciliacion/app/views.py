from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *
from .models import Empleado

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


def editar_expediente(request, id_expediente):
    if not request.session.get('empleado_id'):
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=request.session['empleado_id'])
    if not empleado.es_administrador:
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')

    try:
        # Primero obtenemos el número de expediente usando el id_expediente
        expediente_obj = ConciliacionExpedientes.objects.get(id_expediente=id_expediente)
        expediente_numero = expediente_obj.expediente  # Este es el valor de la llave primaria
        
        if request.method == 'POST':
            # Actualizamos usando el número de expediente (llave primaria)
            ConciliacionExpedientes.objects.filter(expediente=expediente_numero).update(
                junta=request.POST.get('junta'),
                tomo=request.POST.get('tomo'),
                actor_nombre=request.POST.get('actor_nombre'),
                mujer_numero=request.POST.get('mujer_numero'),
                hombre_numero=request.POST.get('hombre_numero'),
                demandado_nombre=request.POST.get('demandado_nombre'),
                mujer_numero_0=request.POST.get('mujer_numero_0'),
                hombre_numero_0=request.POST.get('hombre_numero_0'),
                persona_moral_numero=request.POST.get('persona_moral_numero'),
                iebem=request.POST.get('iebem'),
                servicios_salud=request.POST.get('servicios_salud'),
                poder_ejecutivo=request.POST.get('poder_ejecutivo'),
                ayuntamientos=request.POST.get('ayuntamientos'),
                otros_organismos=request.POST.get('otros_organismos'),
                no_se_ha_notificado_a_las_partes=request.POST.get('no_se_ha_notificado_a_las_partes'),
                empl_no_realizado=request.POST.get('empl_no_realizado'),
                empl_exhorto=request.POST.get('empl_exhorto'),
                exhortos_sin_enviar=request.POST.get('exhortos_sin_enviar'),
                exhortos_cdmx=request.POST.get('exhortos_cdmx'),
                exhortos_foraneos=request.POST.get('exhortos_foraneos'),
                cde=request.POST.get('cde'),
                tercero_llamado_a_juicio=request.POST.get('tercero_llamado_a_juicio'),
                oap=request.POST.get('oap'),
                desahogo_pruebas=request.POST.get('desahogo_pruebas'),
                test_falta_citar=request.POST.get('test_falta_citar'),
                periciales_partes=request.POST.get('periciales_partes'),
                pericial_tercero=request.POST.get('pericial_tercero'),
                inf_falta_hacer=request.POST.get('inf_falta_hacer'),
                inf_falta_desahogar=request.POST.get('inf_falta_desahogar'),
                otras_pruebas=request.POST.get('otras_pruebas'),
                alegatos=request.POST.get('alegatos'),
                prueba_pendiente=request.POST.get('prueba_pendiente'),
                cierre=request.POST.get('cierre'),
                laudo_dictado=request.POST.get('laudo_dictado'),
                absolutorio=request.POST.get('absolutorio'),
                condenatorio=request.POST.get('condenatorio'),
                monto=request.POST.get('monto'),
                auto_ejecucion=request.POST.get('auto_ejecucion'),
                terceria=request.POST.get('terceria'),
                recurso_revision=request.POST.get('recurso_revision'),
                remate=request.POST.get('remate'),
                inactividad_1_anio=request.POST.get('inactividad_1_anio'),
                inactividad_2_anios_mas=request.POST.get('inactividad_2_anios_mas'),
                amparo_indirecto=request.POST.get('amparo_indirecto'),
                amparo_directo_cumpl=request.POST.get('amparo_directo_cumpl'),
                sustitucion_patronal=request.POST.get('sustitucion_patronal'),
                no_interpuesta=request.POST.get('no_interpuesta'),
                prescripcion=request.POST.get('prescripcion'),
                depuracion=request.POST.get('depuracion'),
                regularizar=request.POST.get('regularizar'),
                reviso_capturo=request.POST.get('reviso_capturo')
            )
            
            messages.success(request, 'Expediente actualizado correctamente.')
            return redirect('bienvenida')
        
        return render(request, 'editar_expediente.html', {'expediente': expediente_obj})
        
    except ConciliacionExpedientes.DoesNotExist:
        messages.error(request, 'El expediente no existe.')
        return redirect('bienvenida')
    # Verify admin permissions
    if not request.session.get('empleado_id'):
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=request.session['empleado_id'])
    if not empleado.es_administrador:
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')

    expediente = get_object_or_404(ConciliacionExpedientes, id_expediente=id_expediente)
    
    if request.method == 'POST':
        # Update all fields
        expediente.expediente = request.POST.get('expediente')
        expediente.junta = request.POST.get('junta')
        expediente.tomo = request.POST.get('tomo')
        expediente.actor_nombre = request.POST.get('actor_nombre')
        expediente.mujer_numero = request.POST.get('mujer_numero')
        expediente.hombre_numero = request.POST.get('hombre_numero')
        expediente.demandado_nombre = request.POST.get('demandado_nombre')
        expediente.mujer_numero_0 = request.POST.get('mujer_numero_0')
        expediente.hombre_numero_0 = request.POST.get('hombre_numero_0')
        expediente.persona_moral_numero = request.POST.get('persona_moral_numero')
        expediente.iebem = request.POST.get('iebem')
        expediente.servicios_salud = request.POST.get('servicios_salud')
        expediente.poder_ejecutivo = request.POST.get('poder_ejecutivo')
        expediente.ayuntamientos = request.POST.get('ayuntamientos')
        expediente.otros_organismos = request.POST.get('otros_organismos')
        expediente.no_se_ha_notificado_a_las_partes = request.POST.get('no_se_ha_notificado_a_las_partes')
        expediente.empl_no_realizado = request.POST.get('empl_no_realizado')
        expediente.empl_exhorto = request.POST.get('empl_exhorto')
        expediente.exhortos_sin_enviar = request.POST.get('exhortos_sin_enviar')
        expediente.exhortos_cdmx = request.POST.get('exhortos_cdmx')
        expediente.exhortos_foraneos = request.POST.get('exhortos_foraneos')
        expediente.cde = request.POST.get('cde')
        expediente.tercero_llamado_a_juicio = request.POST.get('tercero_llamado_a_juicio')
        expediente.oap = request.POST.get('oap')
        expediente.desahogo_pruebas = request.POST.get('desahogo_pruebas')
        expediente.test_falta_citar = request.POST.get('test_falta_citar')
        expediente.periciales_partes = request.POST.get('periciales_partes')
        expediente.pericial_tercero = request.POST.get('pericial_tercero')
        expediente.inf_falta_hacer = request.POST.get('inf_falta_hacer')
        expediente.inf_falta_desahogar = request.POST.get('inf_falta_desahogar')
        expediente.otras_pruebas = request.POST.get('otras_pruebas')
        expediente.alegatos = request.POST.get('alegatos')
        expediente.prueba_pendiente = request.POST.get('prueba_pendiente')
        expediente.cierre = request.POST.get('cierre')
        expediente.laudo_dictado = request.POST.get('laudo_dictado')
        expediente.absolutorio = request.POST.get('absolutorio')
        expediente.condenatorio = request.POST.get('condenatorio')
        expediente.monto = request.POST.get('monto')
        expediente.auto_ejecucion = request.POST.get('auto_ejecucion')
        expediente.terceria = request.POST.get('terceria')
        expediente.recurso_revision = request.POST.get('recurso_revision')
        expediente.remate = request.POST.get('remate')
        expediente.inactividad_1_anio = request.POST.get('inactividad_1_anio')
        expediente.inactividad_2_anios_mas = request.POST.get('inactividad_2_anios_mas')
        expediente.amparo_indirecto = request.POST.get('amparo_indirecto')
        expediente.amparo_directo_cumpl = request.POST.get('amparo_directo_cumpl')
        expediente.sustitucion_patronal = request.POST.get('sustitucion_patronal')
        expediente.no_interpuesta = request.POST.get('no_interpuesta')
        expediente.prescripcion = request.POST.get('prescripcion')
        expediente.depuracion = request.POST.get('depuracion')
        expediente.regularizar = request.POST.get('regularizar')
        expediente.reviso_capturo = request.POST.get('reviso_capturo')
        
        expediente.save()
        messages.success(request, 'Expediente actualizado correctamente.')
        return redirect('bienvenida')
    
    return render(request, 'editar_expediente.html', {'expediente': expediente})

def eliminar_expediente(request, id_expediente):
    if not request.session.get('empleado_id'):
        return redirect('iniciar_sesion')
    
    empleado = Empleado.objects.get(id=request.session['empleado_id'])
    if not empleado.es_administrador:
        messages.error(request, 'No tienes permiso para realizar esta acción.')
        return redirect('bienvenida')
    
    expediente = get_object_or_404(ConciliacionExpedientes, id_expediente=id_expediente)
    expediente.delete()
    messages.success(request, 'Expediente eliminado correctamente.')
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


### 4. Implementa las vistas de editar y eliminar

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

