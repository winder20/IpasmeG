# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

# ---------------------------------- Crea tu Modelo ------------------------------------ #

	
	# INSTITUCION #

class Institucion(models.Model):
	institucion = models.AutoField(primary_key=True)
	nombre = models.CharField("Nombre (*)", max_length=40)
	tipo = models.CharField("Tipo (*)", max_length=40)
	fecha_ingreso = models.DateField('Fecha de Ingreso (*)')

	def __str__(self):
		return '{} {}' .format (self.nombre,self.tipo)


