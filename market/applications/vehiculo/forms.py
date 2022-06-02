# django
from django import forms
# local
from .models import  Flete, Rent, Transport

class TransportForm(forms.ModelForm):

    class Meta:
        model = Transport
        fields = {
            'placa',
            'modelo',
            'color',
            'marca',
        }

        Widgets = {
            'placa': forms.TextInput(
                attrs = {
                    'placeholder': 'Placa del vehiculo',
                    'class': 'input-group-field',
                }
            ),

            'modelo': forms.TextInput(
                attrs = {
                    'placeholder': 'Modelo del vehiculo',
                    'class': 'input-group-field',
                }
            ),

            'color': forms.TextInput(
                attrs = {
                    'placeholder': 'Color del vehiculo',
                    'class': 'input-group-field',
                }
            ),

        }


class FleteForm(forms.ModelForm):

    class Meta:
        model = Flete
        fields = (
            'entry_date',
            'company',
            'price',
            'vehiculo',
            'description',
        )

        Widgets = {

            'entry_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),

            'price': forms.TextInput(
                attrs = {
                    'placeholder': 'Precio del flete',
                    'class': 'input-group-field',
                }
            ),

            'description': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripcion del producto',
                    'rows': '3',
                    'class': 'input-group-field',
                }
            ),

        }



class RentaForm(forms.ModelForm):

    class Meta:
        """Meta definition for Rentaform."""

        model = Rent
        fields = (
            'date',
            'price',
            'machine',
            'description',
        )
        widgets = {

            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'input-group-field',
                },
            ),

            'price': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),

            'description': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripcion del producto',
                    'rows': '3',
                    'class': 'input-group-field',
                }
            ),
        }

class VentaForm(forms.ModelForm):

    class Meta:
        """Meta definition for Rentaform."""

        model = Rent
        fields = (
            'price',
            'machine',
            'description',
        )
        widgets = {


            'price': forms.NumberInput(
                attrs = {
                    'placeholder': '1',
                    'class': 'input-group-field',
                }
            ),

            'description': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripcion del producto',
                    'rows': '3',
                    'class': 'input-group-field',
                }
            ),
        }
    