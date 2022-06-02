from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    CreateView,
    DetailView, 
    DeleteView
)
from .models import Contact, Meet
from applications.venta.models import Sale, SaleDetail
from applications.producto.models import Product
from applications.users.mixins import AdminPermisoMixin, AlmacenPermisoMixin
#
from .forms import ContactForm, LiquidacionProviderForm, MeetForm, ResumenVentasForm
#
from .functions import detalle_resumen_ventas




class PanelHomeView(ListView):
    template_name = "home/index.html"
    context_object_name = 'meets'

    def get_queryset(self):

        queryset = Meet.objects.filtrar(
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", '')
        )
        return queryset


class HomePageView(TemplateView):
    template_name = "web/home.html"

class PanelAdminView(AdminPermisoMixin, TemplateView):
    template_name = "home/administrador.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_ventas"] = Sale.objects.total_ventas_dia()
        context["total_anulaciones"] = Sale.objects.total_ventas_anuladas_dia()
        context["stok_cero"] = Product.objects.productos_en_cero().count()
        context["resumen_semana"] = SaleDetail.objects.resumen_ventas()[:7]
        return context
    

class ReporteAdmin(AdminPermisoMixin, ListView):
    template_name = "home/reporte_admin.html"
    context_object_name = "resumen_ventas_mes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_ventas"] = Sale.objects.total_ventas()
        return context
    
    def get_queryset(self):
        return SaleDetail.objects.resumen_ventas_mes()
    


class ReporteLiquidacion(AdminPermisoMixin, ListView):
    template_name = "home/reporte_liquidacion.html"
    context_object_name = "ventas_liquidacion"
    extra_context = {'form': LiquidacionProviderForm}
    
    def get_queryset(self):
        
        lista_ventas, total_ventas = SaleDetail.objects.resumen_ventas_proveedor(
            provider=self.request.GET.get("provider", ''),
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
        )
        self.extra_context.update({'total_ventas': total_ventas})
        return lista_ventas


class ReporteResumenVentas(AdminPermisoMixin, ListView):
    template_name = "home/resumen_ventas.html"
    context_object_name = "resumen_ventas"
    extra_context = {'form': ResumenVentasForm}
    
    def get_queryset(self):
        
        lista_ventas = detalle_resumen_ventas(
            self.request.GET.get("date_start", ''),
            self.request.GET.get("date_end", ''),
        )
        return lista_ventas




class ContactCreateView(AdminPermisoMixin, CreateView):
    form_class = ContactForm
    success_url = '.'

class ListContactView(AdminPermisoMixin, ListView):
    template_name = "home/list_contact.html"
    context_object_name = 'contactos'
    model = Contact

class ContactDetailView(AdminPermisoMixin, DetailView):
    template_name = "home/detail_contact.html"
    model = Contact



class MeetCreateView(AdminPermisoMixin, CreateView):
    template_name = "reuniones/form_reunion.html"
    form_class = MeetForm
    success_url = reverse_lazy('home_app:index')

class MeetListView(AdminPermisoMixin, ListView):
    template_name = "reuniones/list_reuniones.html"
    model = Meet
    context_object_name = 'meets'

class MeetUpdateView(AdminPermisoMixin,UpdateView):
    template_name = "reuniones/update_reunion.html"
    model = Meet
    form_class = MeetForm
    success_url = reverse_lazy('home_app:list_meet')

class MeetDeleteView(AdminPermisoMixin,DeleteView):
    model = Meet
    success_url = reverse_lazy('home_app:list_meet')

