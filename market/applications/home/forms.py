from django import forms

from .models import Contact, Meet
from applications.producto.models import Provider


class LiquidacionProviderForm(forms.Form):

    provider = forms.ModelChoiceField(
        required=True,
        queryset=Provider.objects.all(),
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )


class ResumenVentasForm(forms.Form):
    
    date_start = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )
    date_end = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
                'class': 'input-group-field',
            },
        )
    )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')



class MeetForm(forms.ModelForm):
    
    class Meta:
        model = Meet
        fields = (
            'date',
            'hour',
            'business',
            'group',
        )
        widgets = {
            'date': forms.DateInput(
                format='%Y-%m-%d',
                attrs = {
                    'type': 'date',
                    'class': 'input-group-field',
                }
            ),
            'hour':  forms.NumberInput(
                attrs = {
                    'placeholder': 'Hora de la reunion',
                    'class': 'input-group-field',
                }
            ),
             'business': forms.TextInput(
                attrs = {
                    'placeholder': 'asunto de la reunion...',
                    'class': 'input-group-field',
                }
            ),
            'group': forms.Select(
                attrs = {
                    'class': 'input-group-field',
                }
            ),
        }