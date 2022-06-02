from django.urls import path
from . import views

app_name = "vehiculo_app"

urlpatterns = [

    path(
        'vehiculo/lista/', 
        views.TransporteListView.as_view(),
        name='transporte-lista',
    ),

    path(
        'vehiculo/agregar/', 
        views.TransporteCreateView.as_view(),
        name='transporte-add',
    ),

    path(
        'vehiculo/agregar_flete/', 
        views.FleteCreateView.as_view(),
        name='flete-add',
    ),

    path(
        'vehiculo/filtro_empresa/', 
        views.FiltrosEmpresasListView.as_view(),
        name='filtro',
    ),

    path(
        'maquinaria/renta_maquinaria/', 
        views.RentCreateView.as_view(),
        name='Rent_maquinaria',
    ),

    path(
        'maquinaria/venta_maquinaria/', 
        views.VentCreateView.as_view(),
        name='vent_maquinaria',
    ),

    


]