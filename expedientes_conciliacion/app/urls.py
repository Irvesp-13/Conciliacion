from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('administrador/', views.administrador, name='administrador'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),  # Nueva URL
]