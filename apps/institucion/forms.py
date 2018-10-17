# -*- coding: utf-8 -*-
#!/usr/bin/python

# -------------------------------- Aqui se Importan tus Modelos --------------------------------- #

from django import forms
from .models import *

# ---------------------------------- Crea tu Formulario ------------------------------------ #

	
	# INSTITUCION #

class InstitucionForm(forms.ModelForm):
	class meta : 
		model = models.Institucion
		fields = ('nombre','tipo','fecha_ingreso',)

		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		'tipo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_ingreso': forms.DateInput(attrs={'class':'form-control', 'type':'date'},format= '%Y-%M-D'),
		}