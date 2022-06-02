#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        'panel/', 
        views.PanelHomeView.as_view(),
        name='index',
    ),
    path(
        '', 
        views.HomePageView.as_view(),
        name='home',
    ),
    path(
        'panel/admin/', 
        views.PanelAdminView.as_view(),
        name='index-admin',
    ),
    path(
        'panel/admin-reporte/', 
        views.ReporteAdmin.as_view(),
        name='admin-reporte',
    ),
    path(
        'panel/admin-liquidacion/', 
        views.ReporteLiquidacion.as_view(),
        name='admin-liquidacion',
    ),
    path(
        'panel/admin-resumen-ventas/', 
        views.ReporteResumenVentas.as_view(),
        name='admin-resumen_ventas',
    ),

    path(
        '/contact', 
        views.ContactCreateView.as_view(),
        name='concacto_clientes',
    ),
    path(
        '/list-contact/', 
        views.ListContactView.as_view(),
        name='lista_concacto_clientes',
    ),
    path(
        '/detail-contact/<pk>/', 
        views.ContactDetailView.as_view(),
        name='concact_detail',
    ),

    path(
        '/meeting/', 
        views.MeetCreateView.as_view(),
        name='add_meet',
    ),

    path(
        '/list_meeting/', 
        views.MeetListView.as_view(),
        name='list_meet',
    ),

    path(
        '/update/<pk>/', 
        views.MeetUpdateView.as_view(),
        name='update_meet',
    ),

    path(
        '/Delete/<pk>/', 
        views.MeetDeleteView.as_view(),
        name='delete_meet',
    ),
]