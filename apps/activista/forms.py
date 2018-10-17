from django import forms

from django.forms.widgets import TextInput

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..activista.models import Account

from ..utils.forms_date import DateInput

from ..activista import models


class AccountModelForm(UserCreationForm):

    class Meta:
        model = models.Account
        exclude = ('created_at', 'updated_at', 'groups', 'user_permissions',
            'last_login', 'is_active', 'date_joined', 'password','is_staff','is_superuser')
        widgets = {
            'cedula':forms.TextInput(attrs={'class':'form-control','validate':'NUMEROS,ENTER,ESPACIO','minlength':'8','maxlength':'8'}),
            'nombre':forms.TextInput(attrs={'class':'form-control','validate':'LETRAS,ENTER,ESPACIO','onkeyup':'this.value=this.value.toUpperCase();'}),   
            'apellido':forms.TextInput(attrs={'class':'form-control','validate':'LETRAS,ENTER,ESPACIO','onkeyup':'this.value=this.value.toUpperCase();'}), 
            'fecha_naci':DateInput(format = '%Y-%m-%d'),
                
        }


class AccountUpdateModelForm(UserChangeForm):

    class Meta:
        model = models.Account
        exclude = ('created_at', 'updated_at', 'groups', 'user_permissions',
            'last_login', 'is_active', 'date_joined','is_superuser')
        widgets = {
            'cedula':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),   
            'apellido':forms.TextInput(attrs={'class':'form-control'}), 
            'fecha_naci': DateInput(format = '%Y-%m-%d'),
            'email':forms.TextInput(attrs={'class':'form-control'}), 
           
        }