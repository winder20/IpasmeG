# -*- coding: utf-8 -*-
#!/usr/bin/python

# -------------------------------- Aqui se Importan tus Modelos --------------------------------- #

from django import forms
from .models import *

# ---------------------------------- Crea tu Formulario ------------------------------------ #

	
	# Beneficiario #

class ReposoForm(forms.ModelForm):
	class meta : 
		model = models.Reposo
		fields = ('beneficiario','nombre','tipo',)

		widgets = {
		'beneficiario': forms.TextInput(attrs={'class': 'form-control'}),
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'tipo': forms.TextInput(attrs={'class':'form-control'}),

		}