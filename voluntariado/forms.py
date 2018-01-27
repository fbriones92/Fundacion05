'''
Created on 3 dic. 2017

@author: franklin
'''
from django.forms import ModelForm
from django import forms
#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _
from voluntariado.models import Voluntario, Referencia
from django.forms.fields import DateField
from django.forms.widgets import Select, NumberInput, TextInput, DateInput, EmailInput
#from numbers import Number
#from django.forms.fields import CharField#

class ConsultaForm(forms.Form):
    fecha_inicial = forms.DateField()
    fecha_limite = forms.DateField()
    
    fields = [ 'fecha_inicial', 'fecha_limite']
    
    widgets = {
        'fecha_inicial': DateInput(),
        'fecha_limite': DateInput(),
    } 




class VoluntarioForm(ModelForm):
    class Meta:
        model = Voluntario
        
        fields = ['cedula', 'nombres', 'apellidos', 'edad','sexo',
                  'fecha_nacimiento','convencional','celular','correo',
                  'direccion','ocupacion','carrera','institucion', 'idioma', 
                  'fecha_ingreso', 'estado', 'referencia']
        widgets= {
            'convencional': NumberInput(),
            'celular': NumberInput(),
            'fecha_nacimiento': DateInput(attrs={'class': 'mdl-color-text--orange', 'type':'date'}),
            'fecha_ingreso': DateInput(attrs={'class': 'mdl-color-text--orange', 'type':'date'}),
            'correo': EmailInput(attrs={'type':'email'}),
            }
        
        help_texts = {
            'cedula':'Cedula Ecuatoriana'
        }
        
        
        
class ReferenciaForm(ModelForm):
    class Meta:
        model = Referencia
        fields = '__all__'        
