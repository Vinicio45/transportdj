# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class TransportManager(models.Manager):
    """ procedimiento modelo transporte """

    def buscar_transporte(self, kword, order):
        consulta = self.filter(
            Q(modelo__icontains=kword) 
        )
        # verificamos en que orden se solicita
        if order == 'modelo':
            # ordenar por nombre
            return consulta.order_by('modelo')
        else:
            return consulta.order_by('-created')
    

    def update_stok_ventas_producto(self, venta_id):
        #
        consulta = self.filter(
            product_sale__sale__id=venta_id
        )
        #
        consulta.update(count=(F('count') + 1))
    

    def productos_en_cero(self):
        #
        consulta = self.filter(
           count__lt=10
        )
        #
        return consulta
    

class FleteManager(models.Manager):
    
     def filtrarEmpresa(self, **filters):
        if not filters['date_start']:
            filters['date_start'] = '2020-01-01'
        
        if not filters['date_end']:
            filters['date_end'] = timezone.now().date() + timedelta(1080)
        #
        consulta = self.filter(
            entry_date__range=(filters['date_start'], filters['date_end'])
        ).filter(
            company__name__icontains=filters['company'],
        )

    
        return consulta.order_by('-created')



            