from ast import Return
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)

from applications.users.mixins import AlmacenPermisoMixin,RentaPermisoMixin

from .models import Transport, Flete, Heavy_machinery
from .forms import TransportForm, FleteForm, RentaForm

# Create your views here.

class TransporteListView(RentaPermisoMixin, ListView):
    template_name = "vehiculos/lista_transporte.html"
    context_object_name = 'transportes'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Transport.objects.buscar_transporte(kword, order)
        return queryset


class TransporteCreateView(RentaPermisoMixin, CreateView):
    template_name = "vehiculos/form_transporte.html"
    form_class = TransportForm
    success_url = reverse_lazy('vehiculo_app:transporte-lista')


class FleteCreateView(RentaPermisoMixin, CreateView):
    template_name = "vehiculos/form_flete.html"
    form_class = FleteForm
    success_url = reverse_lazy('vehiculo_app:transporte-lista')



class FiltrosEmpresasListView(RentaPermisoMixin, ListView):
    template_name = "vehiculos/filtro_empresas.html"
    context_object_name = 'transportes'
    
    

    def get_queryset(self):        
        queryset = Flete.objects2.filtrarEmpresa(
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
            company=self.request.GET.get("company", ''),
        )
        return queryset


class RentCreateView(RentaPermisoMixin, CreateView):
    template_name = "maquinaria/form_renta.html"
    form_class = RentaForm
    success_url = reverse_lazy('vehiculo_app:transporte-lista')


class VentCreateView(RentaPermisoMixin, CreateView):
    template_name = "maquinaria/form_venta.html"
    form_class = RentaForm
    success_url = reverse_lazy('vehiculo_app:transporte-lista')

    def create(self, request, *args, **kwargs):
        self.object.is_active = False
        self.object.save()

