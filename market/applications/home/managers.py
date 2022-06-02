# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class MeetManager(models.Manager):
    """ procedimiento modelo product """
    
    def filtrar(self, **filters):
        if not filters['date_start']:
            filters['date_start'] = timezone.now()
        
        if not filters['date_end']:
            filters['date_end'] = '2025-01-01'
        #
        consulta = self.filter(
            date__range=(filters['date_start'], filters['date_end'])
        )

        
        return consulta.order_by('-created')
            

            