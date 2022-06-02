from unicodedata import name
from model_utils.models import TimeStampedModel
# Django
from django.db import models

from .managers import MeetManager

class Contact(TimeStampedModel):
    """Formulario de contacto"""

    full_name = models.CharField(
        'Nombres',
        max_length=60
    )

    email = models.EmailField()

    phone = models.CharField(
        'telefonos',
        max_length=40,
    )

    business = models.CharField(
        'Asunto',
        max_length=60
    )

    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name

class Group(TimeStampedModel):
    "Formulario de grupos"

    name = models.TextField(
        'asunto de la reunion',
        blank=True,
    )

    class Meta:
        verbose_name = 'grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.name
    



class Meet(TimeStampedModel):
    """Formulario de reuniones"""

    date = models.DateField(
        'fecha reunion',
        blank=True, 
        null=True
    )

    hour = models.TextField(
        'hora de la reunion',
        blank=True,
    )
    business = models.TextField(
        'asunto de la reunion',
        blank=True,
    )

    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE
    )

    objects = MeetManager()

    class Meta:
        verbose_name = 'reunion'
        verbose_name_plural = 'reuniones'

    def __str__(self):
        return self.business
    



