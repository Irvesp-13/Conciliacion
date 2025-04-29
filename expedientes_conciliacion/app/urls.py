from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('agregar-expediente/', views.agregar_expediente, name='agregar_expediente'),
    path('editar_expediente/<int:id_expediente>/', views.editar_expediente, name='editar_expediente'),
    path('crear-empleado/', views.crear_empleado, name='crear_empleado'),
    path('editar-empleado/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar-empleado/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('cargar-expediente/', views.cargar_expediente, name='cargar_expediente'),
    path('ver-cargas/', views.ver_cargas, name='ver_cargas'),
]