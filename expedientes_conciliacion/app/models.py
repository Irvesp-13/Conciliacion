from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    clave_empleado = models.CharField(max_length=20, unique=True)
    puesto = models.IntegerField()  # 1: Administrador, 2: Usuario normal

    def __str__(self):
        return self.nombre

    def es_administrador(self):
        return self.puesto == 1

class ConciliacionExpedientes(models.Model):
    expediente = models.CharField(max_length=255, primary_key=True, db_column='EXPEDIENTE')
    junta = models.CharField(max_length=255, blank=True, null=True, db_column='JUNTA')
    tomo = models.CharField(max_length=255, blank=True, null=True, db_column='TOMO')
    actor_nombre = models.CharField(max_length=255, blank=True, null=True, db_column='ACTOR (NOMBRE)')
    mujer_numero = models.CharField(max_length=255, blank=True, null=True, db_column='MUJER (NUMERO)')
    hombre_numero = models.CharField(max_length=255, blank=True, null=True, db_column='HOMBRE (NUMERO)')
    demandado_nombre = models.CharField(max_length=255, blank=True, null=True, db_column='DEMANDADO (NOMBRE)')
    mujer_numero_0 = models.CharField(max_length=255, blank=True, null=True, db_column='MUJER (NUMERO)_[0]')
    hombre_numero_0 = models.CharField(max_length=255, blank=True, null=True, db_column='HOMBRE (NUMERO)_[0]')
    persona_moral_numero = models.CharField(max_length=255, blank=True, null=True, db_column='PERSONA MORAL (NUMERO)')
    iebem = models.CharField(max_length=255, blank=True, null=True, db_column='IEBEM')
    servicios_salud = models.CharField(max_length=255, blank=True, null=True, db_column='SERVICIOS SALUD')
    poder_ejecutivo = models.CharField(max_length=255, blank=True, null=True, db_column='PODER EJECUTIVO')
    ayuntamientos = models.CharField(max_length=255, blank=True, null=True, db_column='AYUNTAMIENTOS')
    otros_organismos = models.CharField(max_length=255, blank=True, null=True, db_column='OTROS ORGANISMOS')
    no_se_ha_notificado_a_las_partes = models.CharField(max_length=255, blank=True, null=True, db_column='NO SE HA NOTIFICADO A LAS PARTES')
    empl_no_realizado = models.CharField(max_length=255, blank=True, null=True, db_column='EMPL.NO REALIZADO')
    empl_exhorto = models.CharField(max_length=255, blank=True, null=True, db_column='EMPL. EXHORTO')
    exhorto_sin_enviar = models.CharField(max_length=255, blank=True, null=True, db_column='EXHORTO SIN ENVIAR')
    exhorto_cdmx = models.CharField(max_length=255, blank=True, null=True, db_column='EXHORTO CDMX')
    exhorto_foraneos = models.CharField(max_length=255, blank=True, null=True, db_column='EXHORTO FORANEOS')
    cde = models.CharField(max_length=255, blank=True, null=True, db_column='C.D.E.')
    tercero_llamado_a_juicio = models.CharField(max_length=255, blank=True, null=True, db_column='TERCERO LLAMADO A JUICIO')
    oap = models.CharField(max_length=255, blank=True, null=True, db_column='O.A.P.')
    desahogo_pruebas = models.CharField(max_length=255, blank=True, null=True, db_column='DESAHOGO PRUEBAS')
    test_falta_citar = models.CharField(max_length=255, blank=True, null=True, db_column='TEST. FALTA CITAR')
    periciales_partes = models.CharField(max_length=255, blank=True, null=True, db_column='PERICIALES PARTES')
    pericial_tercero = models.CharField(max_length=255, blank=True, null=True, db_column='PERICIAL TERCERO')
    inf_falta_hacer = models.CharField(max_length=255, blank=True, null=True, db_column='INF. FALTA HACER')
    inf_falta_desahogar = models.CharField(max_length=255, blank=True, null=True, db_column='INF. FALTA DESAHOGAR')
    otras_pruebas = models.CharField(max_length=255, blank=True, null=True, db_column='OTRAS PRUEBAS')
    alegatos = models.CharField(max_length=255, blank=True, null=True, db_column='ALEGATOS')
    prueba_pendiente = models.CharField(max_length=255, blank=True, null=True, db_column='PRUEBA PENDIENTE')
    cierre = models.CharField(max_length=255, blank=True, null=True, db_column='CIERRE')
    laudo_dictado = models.CharField(max_length=255, blank=True, null=True, db_column='LAUDO DICTADO')
    absolutorio = models.CharField(max_length=255, blank=True, null=True, db_column='ABSOLUTORIO')
    condenatorio = models.CharField(max_length=255, blank=True, null=True, db_column='CONDENATORIO')
    monto = models.CharField(max_length=255, blank=True, null=True, db_column='MONTO')
    auto_ejecucion = models.CharField(max_length=255, blank=True, null=True, db_column='AUTO EJECUCCION')
    terceria = models.CharField(max_length=255, blank=True, null=True, db_column='TERCERIA')
    recurso_revision = models.CharField(max_length=255, blank=True, null=True, db_column='RECURSO REVISION')
    remate = models.CharField(max_length=255, blank=True, null=True, db_column='REMATE')
    inactividad_1_anio = models.CharField(max_length=255, blank=True, null=True, db_column='INACTIVIDAD 1 ANIO')
    inactividad_2_anios_mas = models.CharField(max_length=255, blank=True, null=True, db_column='INACTIVIDAD 2 ANIOS MAS')
    amparo_indirecto = models.CharField(max_length=255, blank=True, null=True, db_column='AMPARO INDIRECTO')
    amparo_directo_cumpl = models.CharField(max_length=255, blank=True, null=True, db_column='AMP. DIRECTO CUMPL')
    sustitucion_patronal = models.CharField(max_length=255, blank=True, null=True, db_column='SUSTITUCION PATRONAL')
    no_interpuesta = models.CharField(max_length=255, blank=True, null=True, db_column='NO INTERPUESTA')
    prescripcion = models.CharField(max_length=255, blank=True, null=True, db_column='PRESCRIPCION')
    depuracion = models.CharField(max_length=255, blank=True, null=True, db_column='DEPURACION')
    regularizar = models.CharField(max_length=255, blank=True, null=True, db_column='REGULARIZAR')
    reviso_y_capturo = models.CharField(max_length=255, blank=True, null=True, db_column='REVISO Y CAPTURO')

    class Meta:
        db_table = 'concilacion_expadientes'  # Nombre de la tabla en MySQL
        managed = False  # Evita que Django intente gestionar la tabla