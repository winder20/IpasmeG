# -*- coding: utf-8 -*-
#!/usr/bin/python

# -------------------------------- Aqui se Importan tus Modelos --------------------------------- #

from django import forms
from .models import *

# ---------------------------------- Crea tu Formulario ------------------------------------ #

	
	# Beneficiario #

class BeneficiarioForm(forms.ModelForm):
	class meta : 
		model = models.Beneficiario
		fields = ('afiliado','cedula_beneficiario','nombres','apellidos','profecion_beneficiario','sitio_traba','ingre_mensu_beneficiario','correo','telefono','movil',)

		widgets = {
		'afiliado': forms.TextInput(attrs={'class': 'form-control'}),
		'cedula_beneficiario': forms.TextInput(attrs={'class':'form-control'}),
		'nombres': forms.TextInput(attrs={'class':'form-control'}),
		'apellidos': forms.TextInput(attrs={'class':'form-control'}),
		'profecion_beneficiario': forms.TextInput(attrs={'class':'form-control'}),
		'sitio_traba': forms.TextInput(attrs={'class':'form-control'}),
		'ingre_mensu_beneficiario': forms.TextInput(attrs={'class':'form-control'}),
		'correo': forms.TextInput(attrs={'class':'form-control'}),
		'telefono': forms.TextInput(attrs={'class':'form-control'}),
		'movil': forms.TextInput(attrs={'class':'form-control'}),
		


		}

	