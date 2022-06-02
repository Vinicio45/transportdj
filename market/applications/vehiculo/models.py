# third-party
#from turtle import color
from itertools import product
from tkinter import CASCADE
from model_utils.models import TimeStampedModel
# Django
from django.db import models
# local
from .managers import TransportManager,FleteManager

class Marca(TimeStampedModel):
    """
        Marca de un vehiculo
    """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Empresa(TimeStampedModel):
    """
        empresa
    """

    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name


class Transport(TimeStampedModel):

    placa = models.CharField(
        'placa', 
        max_length=10
    )

    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE
    )

    modelo = models.CharField(
        'modelo',
        max_length=30
    )

    color = models.CharField(
        'color',
        max_length=30
    )

    objects = TransportManager()

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'

    def __str__(self):
        return self.placa


class Flete(TimeStampedModel):

    entry_date = models.DateField(
        'fehca de transaccion ',
        blank=True, 
        null=True
    )

    company = models.ForeignKey(
       Empresa, 
       on_delete=models.CASCADE
    )

    price = models.DecimalField(
        'precio del flete',
        max_digits=7, 
        decimal_places=2
    )

    vehiculo = models.ForeignKey(
       Transport, 
       on_delete=models.CASCADE
    )

    description = models.TextField(
        'descripcion del viaje',
        blank=True,
    )

    objects2 = FleteManager()

    class Meta:
        verbose_name = 'Flete'
        verbose_name_plural = 'Fletes'

    def __str__(self):
        return self.description






class Heavy_machinery(TimeStampedModel):

    description = models.CharField(
        'descripcion', 
        max_length=60
    )

    is_active = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Maquinaria'
        verbose_name_plural = 'Maquinarias'

    def __str__(self):
        return self.description


class Rent(TimeStampedModel):
    
    date = models.DateField(
        'fehca de transaccion ',
        blank=True, 
        null=True
    )

    price = models.DecimalField(
        'precio de la renta',
        max_digits=7, 
        decimal_places=2
    )

    machine = models.ForeignKey(
       Heavy_machinery, 
       on_delete=models.CASCADE
    )

    description = models.TextField(
        'descripcion',
        blank=True,
    )


class Sale(TimeStampedModel):
    
    price = models.DecimalField(
        'precio de la renta',
        max_digits=7, 
        decimal_places=2
    )

    machine = models.ForeignKey(
       Heavy_machinery, 
       on_delete=models.CASCADE
    )

    description = models.TextField(
        'descripcion',
        blank=True,
    )


