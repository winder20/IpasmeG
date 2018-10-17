# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from ..afiliado.models import Afiliado

# ---------------------------------- Crea tu Modelo ------------------------------------ #

class Beneficiario(models.Model):
	beneficiario=models.AutoField(primary_key=True)
	afiliado = models.ForeignKey(Afiliado, verbose_name='Afiliado (*)')
	cedula_beneficiario=models.CharField(verbose_name='Cedula (*)',max_length=8, unique=True, null=True)
	nombres=models.CharField(verbose_name='Nombres (*)',max_length=40, null=True)
	apellidos=models.CharField(verbose_name='Apellidos (*)',max_length=40, null=True)
	profecion_beneficiario= models.CharField(verbose_name='Profesion (*)',max_length=200, null=True)
	sitio_traba = models.CharField(verbose_name='Sitio de Trabajo (*)',max_length=200,null=True)
	ingre_mensu_beneficiario = models.CharField(verbose_name='Ingreso Mensual (*)',max_length=100,null=True)
	correo= models.EmailField(verbose_name='Correo Electronico (*)',max_length=100, null=True)
	telefono=models.CharField(verbose_name='Telefono (*)',max_length=7)
	movil=models.CharField(verbose_name='Movil (*)',max_length=7,null=True)
	
	def __str__(self):
		return '{} {} {}' .format (self.cedula_beneficiario,self.nombres,self.apellidos)
