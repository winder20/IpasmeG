# -*- coding: utf-8 -*-
#!/usr/bin/python

# -------------------------------- Aqui se Importan tus Modelos --------------------------------- #
from django import forms
from .models import *
from .models import Afiliado
from ..utils.forms_date import  DateInput


# ---------------------------------- Crea tu Formulario ------------------------------------ #

	
	# Afiliado #
class AfiliadoForm(forms.ModelForm):
	class meta : 
		model = models.Afiliado
		fields = [
			'institucion',
			'cedula_afiliado',
			'nombres',
			'apellidos',
			'num_familia',
			'direccion',
			'profecion_afiliado',
			'sitio_traba',
			'ingre_mensu_afiliado',
			'correo',
			'telefono',
			'movil',
			'sector',
			'comunidad',
			'avenidad',
			'calle',
			'casa',
		]

		labels = {
			'institucion': 'Institucion',
			'cedula_afiliado':'Cedula del Afiliado',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'num_familia': 'Numero de Familia',
			'direccion': 'Direccion',
			'profecion_afiliado',
			'sitio_traba': 'Sitio de Trabajo',
			'ingre_mensu_afiliado': 'Ingreso Mensual del Afiliado',
			'correo': 'Correo',
			'telefono': 'Telefono',
			'movil': 'Movil',
			'sector': 'Sector',
			'comunidad': 'Comunidad',
			'avenidad':'Avenidad',
			'calle': 'Calle',
			'casa': 'Casa',

		}

		widgets = {
			'institucion': forms.TextInput(attrs={'class': 'form-control'}),
			'cedula_afiliado': forms.TextInput(attrs={'class':'form-control'}),
			'nombres': forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'num_familia': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'profecion_afiliado': forms.TextInput(attrs={'class':'form-control'}),
			'sitio_traba': forms.TextInput(attrs={'class':'form-control'}),
			'ingre_mensu_afiliado': forms.TextInput(attrs={'class':'form-control'}),
			'correo': forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'movil': forms.TextInput(attrs={'class':'form-control'}),
			'sector': forms.TextInput(attrs={'class':'form-control'}),
			'comunidad': forms.TextInput(attrs={'class':'form-control'}),
			'avenidad': forms.TextInput(attrs={'class':'form-control'}),
			'calle': forms.TextInput(attrs={'class':'form-control'}),
			'casa': forms.TextInput(attrs={'class':'form-control'}),


		}
