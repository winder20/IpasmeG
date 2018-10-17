# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from ..beneficiario.models import Beneficiario

# ---------------------------------- Crea tu Modelo ------------------------------------ #


class Reposo(models.Model):
	reposo = models.AutoField(primary_key=True)
	beneficiario = models.ForeignKey(Beneficiario, verbose_name='Beneficiario')
	nombre = models.CharField(verbose_name='Reposo (*)', max_length=50)
	tipo = models.CharField(verbose_name='Tipo (*)', max_length=50)

	def __str__(self):
		return '{} {} {}'.format (self.nombre, self.tipo, self.beneficiario)